#!/usr/bin/env python
# encoding: utf-8
'''
Created on 19 Apr 2015

@author: "Waldemar Zurowski"
'''

import logging
import botocore.session
from botocore.hooks import HierarchicalEmitter
from awscli.customizations.assumerole import register_assume_role_provider
from awscli.customizations.scalarparse import register_scalar_parser


logging.basicConfig(level=logging.DEBUG)

emitter = HierarchicalEmitter()
session = botocore.session.Session(event_hooks=emitter)
register_assume_role_provider(emitter)
register_scalar_parser(emitter)
session.emit('session-initialized', session=session)


client = session.create_client('ec2', region_name='eu-west-1')
print session.full_config

for reservation in client.describe_instances()['Reservations']:
    for instance in reservation['Instances']:
        print instance['InstanceId']
