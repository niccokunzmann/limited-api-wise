"""The command line interface to start the application."""

import uvicorn

from limited_api_wise.app import app
from limited_api_wise.settings import Settings


def check_profile_id():
    """List the available profiles on Wise if the id is not available."""
    profiles = Settings.get().client.profiles.list()
    if not any(profile.id == Settings.get().profile_id for profile in profiles):
        print("You need to start the app with a profile id. Copy one from here:")
        for profile in profiles:
            name = f"{profile.details.firstName} {profile.details.lastName}" if profile.type == "personal" else profile.details.name
            print(f"profile_id: {profile.id} type: {profile.type} name: {name}")
        raise ValueError("Invalid profile_id in settings.")


def main():
    """Run the application."""
    check_profile_id()
    uvicorn.run(app, host=Settings.get().host, port=Settings.get().port)


if __name__ == "__main__":
    main()
