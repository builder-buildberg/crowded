from django.core.management.base import BaseCommand
import gspread
from gspread_dataframe import get_as_dataframe
from ground.models import Ground
from django.core.files import File
from PIL import Image, ImageDraw
import requests
from io import BytesIO, StringIO

class Command(BaseCommand):

    help = 'Import data from google sheet'

    def handle(self, *args, **options):
        # Authenticate with Google Sheets API
        # get the filename from the root directory of the
        # project
        Ground.objects.all().delete()
        gc = gspread.service_account(filename='service_account.json')
        # Open the spreadsheet
        sh = gc.open("Grounds")
        # Get the first sheet
        worksheet = sh.sheet1
        # Get the data
        data = get_as_dataframe(worksheet)

        # Iterate through the rows of the dataframe
        for index, row in data.iterrows():
            # make sure the ground doesn't already exist
            if not Ground.objects.filter(name=row['name']).exists():
                # create the ground
                ground = Ground(
                    name=row['name'],
                    address=row['address'],
                    area=row['area'],
                    city=row['city'],
                    num_of_courts=row['num_of_courts'],
                    sports_type=row['sports_type'],
                    owner_contact=int("0"+str(row['owner_contact'])),
                    price=row['price'],
                    # has_lights is a boolean field but in sheets it is TRUE FALSE
                    # so we need to convert it to boolean
                    has_lights=row['has_lights'] == 'TRUE',
                    has_drinks=row['has_drinks'] == 'TRUE',
                    map_link=row['map_link'],
                    should_also_be_shown_in=row['should_also_be_shown_in'],
                )

                # Check if image URL is not empty
                if not str(row['image_url']).startswith('http'):
                    # Set the image filename and size
                    image_filename = f'{row["name"]}.webp'
                    image_size = (300, 300)

                    # Create a new image with the white background
                    image = Image.new('RGB', image_size, 'white')

                    # Draw the ground name in the center of the image
                    draw = ImageDraw.Draw(image)

                    text_size = draw.textsize(row['name'])
                    text_position = ((image_size[0] - text_size[0]) // 2, (image_size[1] - text_size[1]) // 2)
                    draw.text(text_position, row['name'], fill='black')

                    # Save the image to the ground's image field
                    image_file = BytesIO()
                    image.save(image_file, 'webp')
                    ground.image.save(image_filename, File(image_file))
                else:
                    # Download the image to a webp format
                    image_url = row['image_url']
                    image_filename = f'{row["name"]}.webp'
                    response = requests.get(image_url)
                    image_data = response.content

                    image = Image.open(BytesIO(image_data))
                    if image.format != 'webp':
                        webp_data = BytesIO()
                        image.save(webp_data, 'webp')
                        image_data = webp_data.getvalue()
                    ground.image.save(image_filename, BytesIO(image_data))
