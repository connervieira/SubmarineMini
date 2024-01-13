# Configuration

This file contains descriptions of all configuration values found in the "config.json" file.

- `general` contains miscellaneous settings for the general operation of Submarine Mini.
    - `interval` is a number that determines how many seconds Submarine Mini will wait between status checks.
        - The higher this number is, the less frequently Submarine will ping the configured targets.
- `targets` contains a list of network targets that Submarine Mini will monitor. Each target uses the IP address/domain of the network device as the key, and contains the following attributes:
    - `name` is a human-readable name for the target.
    - `priority` is an integer number ranging from 0 to 5, where 5 indicates the most importance, and 0 represents the least importance.
        - This value is currently unused, but will likely be used to customize notification behavior in the future.
    - `description` this is a brief, human-readable description of the target.
- `notifications` contains settings for configuring notifications through NTFY
    - `host` is the URL (including the topic name) that will be used to publish notifications through NTFY.
