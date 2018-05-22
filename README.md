# Web Monitor

Get notified when a website updates/is down.

## Features
* Detects if website is up or returning a valid status
* Detects html changes
* Able to notify multiple emails
* Uses sendgrid api to send notification mails.

## Usage
1. export your sendgrid api key to env variable `SENDGRID_API_KEY`
2. Set your settings in `settings.py`
3. Run `monitor.py`
> Use `nohup ./monitor.py &` if you want to run it in the background.
