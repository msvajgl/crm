from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from contacts.services import sync_google_other_contacts

User = get_user_model()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--max-results",
            type=int,
            default=1000,
            help="Maximum number of results to sync",
        )

    def handle(self, *args, **options):
        max_results = options.get("max_results")

        users_qs = User.objects.filter(google_oauth_token__access_token__isnull=False)
        self.stdout.write(
            self.style.SUCCESS(
                f"Sync google contacts starting {max_results} for each {users_qs.count()} users"
            )
        )
        success_count = 0
        fail_count = 0
        for user in users_qs:
            try:
                sync_google_other_contacts(user, max_results=max_results)
                success_count += 1
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"Failed to sync contacts for {user}:\n{e}")
                )
                fail_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"\n Succesfully synced: {success_count} of {users_qs.count()}"
            )
        )
        if fail_count > 0:
            self.stdout.write(
                self.style.ERROR(
                    f"\n Failed synced: {fail_count} of {users_qs.count()}"
                )
            )
