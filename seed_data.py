from faker import Faker

from TODOApp.models import TodoItem

fake = Faker()

print('Seeding data...')


def seed_data():
    for _ in range(10):
        TodoItem.objects.create(
            title=fake.sentence(),
            description=fake.paragraph(),
        )


print('Data seeded successfully!')
