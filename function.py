import pixivapi
import datetime
from pixivapi import models

def fetch_illus_information(client):
    illustration_id = input("Illustration ID : ")
    pic = client.fetch_illustration(illustration_id)
    print()
    print(f"Title : {pic.title}")
    print(f"Type : {pic.type}")
    print(f"Create Date : {pic.create_date}")
    print(f"Artist Detail :")
    print(f"- Name : {pic.user.name}")
    print(f"- Account Name : {pic.user.account}")
    print(f"- Account ID : {pic.user.id}")
    print(f"- Profile Image URL : {pic.user.profile_image_urls}")
    print(f"- Followed? : {pic.user.is_followed}")
    print(f"Tags : {pic.tags}")
    print(f"ID : {pic.id}")
    print(f"Tools : {pic.tools}")
    print(f"Series : {pic.series}")
    print(f"Width * Height : {pic.width} * {pic.height}")
    print(f"Page Number : {pic.page_count}")
    print(f"Restrict : {pic.restrict}")
    print(f"X-Restrict : {pic.x_restrict}")
    print(f"Sanity Level : {pic.sanity_level}")
    print(f"Visibility : {pic.visible}")
    print(f"Total Views : {pic.total_view}")
    print(f"Total Bookmark : {pic.total_bookmarks}")
    print("Caption :")
    print(pic.caption)
    print(f"Total Comments : {pic.total_comments}")
    print()
    print(f"This picture about you ->")
    print(f"Bookmarked? : {pic.is_bookmarked}")
    print(f"Muted? : {pic.is_muted}")
    print()
    print("That's all!")
    print()