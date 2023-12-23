## Configuration

Before running the application, you need to set your API key as an environment variable. Here's how you can do it:

1. Open your `.bashrc` or `.bash_profile` file:

    ```bash
    nano ~/.bashrc  # or `nano ~/.bash_profile` if you're on macOS
    ```

2. Add the following line to the file:

    ```bash
    export API_KEY=your_api_key
    ```

    Replace `your_api_key` with your actual API key.

3. Save and close the file.

4. Apply the changes:

    ```bash
    source ~/.bashrc  # or `source ~/.bash_profile` if you're on macOS
    ```

Now, every time you open a new terminal session, the `API_KEY` environment variable will be set automatically.

## Deployment

To deploy the application on a Linux server with systemd, follow these steps:

1. Create a new service file in `/etc/systemd/system/` with a `.service` extension, for example, `myapp.service`:

    ```bash
    sudo nano /etc/systemd/system/myapp.service
    ```

2. Add the following content to the service file:

    ```ini
    [Unit]
    Description=Gunicorn instance to serve myapp
    After=network.target

    [Service]
    User=yourusername
    Group=www-data
    WorkingDirectory=/path/to/your/app
    Environment="PATH=/path/to/your/app/env/bin"
    ExecStart=/path/to/your/app/env/bin/gunicorn -w 4 server:app

    [Install]
    WantedBy=multi-user.target
    ```

    Replace `yourusername` with your actual username, and `/path/to/your/app` with the actual path to your Flask application.

3. Save and close the file.

4. Start the Gunicorn service you just created:

    ```bash
    sudo systemctl start myapp
    ```

5. Enable the service to start on boot:

    ```bash
    sudo systemctl enable myapp
    ```

6. Check the status of the service:

    ```bash
    sudo systemctl status myapp
    ```

This will ensure that your Flask application starts on boot and restarts if it crashes.