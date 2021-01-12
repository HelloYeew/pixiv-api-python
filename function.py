from pathlib import Path
from pixivapi import Size
import datetime
from pixivapi import ContentType
from tqdm import tqdm
import os

# turn on and turn off dev mode here
dev = False


def fetch_illus_information(client, illustration_id):
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
    if len(pic.tags) == 0:
        print("Tags : No tags")
    else:
        print(f"Tags : {len(pic.tags)} tags include")
        for i in range(len(pic.tags)):
            print(f"{i + 1}.{pic.tags[i]['name']} ({pic.tags[i]['translated_name']})")
    print(f"ID : {pic.id}")
    if len(pic.tools) == 0:
        print("Tools : No Information")
    else:
        print(f"Tools : {len(pic.tools)} tools include")
        for i in range(len(pic.tools)):
            print(f"{i + 1}.{pic.tools[i]}")
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
    fetch_related_illustration(client,illustration_id)
    print("--About the artist")
    fetch_user_information(client, pic.user.id)
    # full_user_data = input(print("Do you want to see a full data of this artist? (y/n) : "))
    # if full_user_data == "y":
    #     fetch_user_information(client, pic.user.id)
    print()


def fetch_user_information(client, user_id):
    user = client.fetch_user(user_id)
    profile_dict = user.profile
    profile_status = user.profile_publicity
    workspace = user.workspace
    print()
    print(f"-> SNS")
    print(f"Twitter name : {profile_dict['twitter_account']}")
    print(f"Twitter URL : {profile_dict['twitter_url']}")
    print(f"Webpage : {profile_dict['webpage']}")
    print(f"Pawoo URL : {profile_dict['pawoo_url']}")
    print()
    print(f"-> Profile")
    print(f"Using Custom Profile? : {profile_dict['is_using_custom_profile_image']}")
    print(f"Background Image URL : {profile_dict['background_image_url']}")
    print(f"Gender : {profile_dict['gender']}")
    print(f"Birth : {profile_dict['birth']}")
    print(f"Birth Day : {profile_dict['birth_day']}")
    print(f"Birth Year : {profile_dict['birth_year']}")
    print(f"Address ID : {profile_dict['address_id']}")
    print(f"Region : {profile_dict['region']}")
    print(f"Country Code : {profile_dict['country_code']}")
    print(f"Job : {profile_dict['job']}")
    print(f"Job ID : {profile_dict['job_id']}")
    print(f"Total Follow Users : {profile_dict['total_follow_users']}")
    print(f"Total Illustration : {profile_dict['total_illusts']}")
    print(f"Total Illustration Series : {profile_dict['total_illust_series']}")
    print(f"Total Illustration Bookmarks Public : {profile_dict['total_illust_bookmarks_public']}")
    print(f"Total Manga : {profile_dict['total_manga']}")
    print(f"Total Novel : {profile_dict['total_novels']}")
    print(f"Total Novel Series : {profile_dict['total_novel_series']}")
    print(f"Total Mypixiv Users : {profile_dict['total_mypixiv_users']}")
    print()
    print(f"-> Profile Publicity")
    print(f"Birth Day : {profile_status['birth_day']}")
    print(f"Birth Year : {profile_status['birth_year']}")
    print(f"Gender : {profile_status['gender']}")
    print(f"Job : {profile_status['job']}")
    print(f"Pawoo : {profile_status['pawoo']}")
    print(f"Region : {profile_status['region']}")
    print()
    print(f"-> Workspace")
    print(f"Chair : {workspace['chair']}")
    print(f"Desk : {workspace['desk']}")
    print(f"Desktop : {workspace['desktop']}")
    print(f"Monitor : {workspace['monitor']}")
    print(f"Mouse : {workspace['mouse']}")
    print(f"Music : {workspace['music']}")
    print(f"PC : {workspace['pc']}")
    print(f"Printer : {workspace['printer']}")
    print(f"Scanner : {workspace['scanner']}")
    print(f"Tablet : {workspace['tablet']}")
    print(f"Tool : {workspace['tool']}")
    print(f"Workspace Image URL : {workspace['workspace_image_url']}")
    print()


def download_all_illustration(client, artist_id):
    response = client.fetch_user_illustrations(artist_id, content_type=ContentType.ILLUSTRATION, offset=None)
    artist_name = response['illustrations'][0].user.name
    directory = Path.cwd() / 'Download' / artist_name
    if dev:
        print(response)
        print(len(response['illustrations']))
    if response['next'] is not None:
        print(f"Downloading... (Total {len(response['illustrations']) + int(response['next'])} illustrations)")
    else:
        print(f"Downloading... (Total {len(response['illustrations'])} illustrations)")
    while True:
        for illust in response['illustrations']:
            illust.download(directory=directory, size=Size.ORIGINAL)

        if not response['next']:
            break

        response = client.fetch_user_illustrations(
            artist_id,
            offset=response['next'],
        )
    print("Complete!")
    print(f"The downloaded content is in {os.getcwd()}/Download/{artist_name}")
    os.system(f"open {os.getcwd()}/Download/{artist_name}")
    print()


def fetch_related_illustration(client, illustration_id):
    response = client.fetch_illustration_related(illustration_id)
    if dev:
        print(response)
        print(len(response['illustrations']))
    print("--Related Illustration")
    for i in range(len(response['illustrations'])):
        picture = response['illustrations'][i]
        print(f"{i+1}.{picture.title} by {picture.user.name} ({picture.id})")
    if response['next'] != None:
        print(f"Next : {response['next']} results")
    else:
        print(f"No more results")
    print()

def illustration_ranking(client):
    response = client.fetch_illustration_ranking()
    if dev:
        print(response)
        print(len(response['illustrations']))
    print("--Related Illustration")
    for i in range(len(response['illustrations'])):
        picture = response['illustrations'][i]
        tag = ""
        for j in picture.tags:
            tag_plus = f"{picture.tags[j]['name']} ({picture.tags[i]['translated_name']}),"
            tag += tag_plus
        print(f"{i+1}.{picture.title} by {picture.user.name} ({picture.id}) [Tag : ")
    if response['next'] != None:
        print(f"Next : {response['next']} results")
    else:
        print(f"No more results")
    print()