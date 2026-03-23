# config.py v1.0.5

config = {
    
    # TMDb API key (required to fetch metadata like title, poster, etc.)
    # Get your API key here: https://www.themoviedb.org/settings/api
    "TMDb": {
        "API_KEY": ""
    },

    # Enable/disable IMDb & TMDb info in description
    "imdb_and_tmdb_info": "True",
    
    # Directory where upload logs will be stored
    "uploads_logs_directory": "Downloads/BWT-Uploader/Uploads",
    
    # Number of screenshots to capture from the video file
    "screenshots_number": 6,
    
    # Number of parallel upload threads
    "upload_threads": 3,

    # Primary image hosting service
    # Options: Freeimage, Imgbb, Imageride, Lookmyimg, Onlyimg, PTScreen
    "image_host": "Imageride",
    
    # Fallback image hosts (used if primary fails)
    "fallback_image_host": "Imgbb",
    "fallback_image_host_2": "Freeimage",

    # API keys for image hosting services (fill only what you use)
    "image_host_api_key": {
        "Freeimage": "",
        "Imgbb": "",
        "Imageride": "",
        "Lookmyimg": "",
        "Onlyimg": "",
        "PTScreen": ""
    },

    # BWTorrents account configuration
    "BWTorrents": {
        "base_url": "https://bwtorrents.tv",
        # Alternative domains:
        # https://bwtorrents.cc
        # https://bwtorrents.xyz
        # https://bwtorrents.us

        "announce_url": "https://bwtorrents.tv/announce.php",
        
        # Your login credentials
        "username": "",
        "password": ""
    },

    # BBCode styling configuration for torrent description
    "bbcode": {

        # Media info banners
        "mediainfo_banner": "[img]https://i.ibb.co/DfF7Pbt/Media-Info.png[/img]",
        "bdinfo_banner": "[img]https://i.ibb.co/DfF7Pbt/Media-Info.png[/img]",
        "dvdinfo_banner": "[img]https://i.ibb.co/DfF7Pbt/Media-Info.png[/img]",
        
        # Section headers styling
        "sections": {
            "general": "[b][color=green]★ General ★[/color][/b]",
            "video": "[b][color=blue]★ Video Track ★[/color][/b]",
            "audio": "[b][color=orange]★ Audio Track ★[/color][/b]",
            "subtitle": "[b][color=teal]★ Subtitle ★[/color][/b]",
            "chapters": "[b][color=red]★ Chapters ★[/color][/b]"
        },

        # Banner displayed above screenshots
        "screenshot_banner": "[img]https://i.ibb.co/9vZTnQk/Screenshot.png[/img]"
    },
}


# Default BBCode template for torrent description
# DO NOT remove placeholders:
# {header}, {file_name}, {media_info}, {screenshot_header}, {screenshot_bbcode}

BBCODE_TEMPLATE = """
{header}

[center]
[b][size=4][color=red]
[font=Arial]{file_name}[/font][/color]
[/size][/b]

{media_info}

{screenshot_header}

{screenshot_bbcode}

[b][size=5][color=green][font=Courier New]
....Enjoying & Keep Seeding....
[/font][/color][/size][/b]
[/center]
"""
