# Celery Based Giveaway Requests Notifications App

## Name: Celery Notif

Celery Notif is a Django web application that demonstrates how to use Celery to work asynchronously and save notifications to the notifications model. This means that users do not have to wait for the page to load and can see that the notification is being sent in the background.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Credits](#credits)
- [License](#license)

## Installation

To install and run Celery Notif, follow these steps:

1. Clone the repository to your local machine: `git clone https://github.com/egenius01/celery_notif.git`
2. Install the necessary dependencies: `pip install -r requirements.txt`
3. Set up a Celery worker: `celery -A celery_notif worker -l info`
4. Run the Django development server: `python manage.py runserver`
5. Open your web browser and go to http://localhost:8000 to view the app.

## Usage

To use Celery Notif, follow these steps:

1. Click on the "Notifications" button to view your notifications.
2. Create a new notification by filling out the single input form and clicking "Send".
3. You should see a message that the notification is being sent in the background.
4. Check the "Notifications" page to see that your notification has been saved to the notifications model.

## Contributing

If you'd like to contribute to Celery Notif, please follow these steps:

1. Fork the repository.
2. Create a new branch for your changes: `git checkout -b feature/your-feature-name`
3. Make your changes and commit them: `git commit -m "Add your commit message here"`
4. Push your changes to your fork: `git push origin feature/your-feature-name`
5. Create a pull request from your fork to the main repository.

## Credits

Celery Notif was created by [Your Name](https://github.com/your-username).

## License

Celery Notif is licensed under the [MIT License](LICENSE).```

