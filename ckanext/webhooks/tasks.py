import db
import json
import logging
import requests
import ckan.model as models

from pylons import config

log = logging.getLogger(__name__)

def notify_hooks(resource, webhook, site_url):
    log.info('Firing webhooks for {0}'.format(webhook['topic']))

    payload = {
        'entity': resource,
        'address': webhook['address'],
        'webhook_id': webhook['id'],
        'ckan': site_url,
        'topic': webhook['topic'],
        'user_ref': webhook['user_id'],
    }

    requests.post(webhook['address'], headers={
            'Content-Type': 'application/json'
        },
        data=json.dumps(payload),
        timeout=2
    )
