import logging

from events import Events as BaseEvents


class Events(BaseEvents):
    __events__ = (
      'on_run_tap_success',
      'on_run_tap_failed',
      'on_schema_created',
      'on_table_created',
      'on_permissions_granted')

    def __init__(self, events_config):
        """
        """
        self.logger = logging.getLogger('Pipelinewise CLI')
        self.events_config = events_config

        self.on_run_tap_success += self.fire_action_on_run_tap_success
        self.on_run_tap_failed += self.fire_action_on_run_tap_failed
        self.on_schema_created += self.fire_action_on_schema_created
        self.on_table_created += self.fire_action_on_table_created
        self.on_permissions_granted += self.fire_action_on_permissions_granted


    def fire_action_on_run_tap_success(self, target, tap, log_file=None):
        self.fire_actions('on_run_tap_success', target=target, tap=tap, log_file=log_file)


    def fire_action_on_run_tap_failed(self, target, tap, log_file=None):
        self.fire_actions('on_run_tap_failed', target=target, tap=tap, log_file=log_file)


    def fire_action_on_schema_created(self, target, tap, schema):
        self.fire_actions('on_schema_created', target=target, tap=tap, schema=schema)


    def fire_action_on_table_created(self, target, tap, schema, table):
        self.fire_actions('on_table_created', target=target, tap=tap, schema=schema, table=table)


    def fire_action_on_permissions_granted(self, db_object, grantee):
        self.fire_actions('on_permissions_granted', object=db_object, grantee=grantee)


    def fire_actions(self, event_name,
        target=None,
        tap=None,
        log_file=None,
        error_message=None,
        schema=None,
        table=None,
        db_object=None,
        grantee=None):
        """
        """
        actions = self.events_config.get(event_name, [])
        #self.logger.info("target: {} - tap: {}".format(target, tap))

        for action in actions:
            run_command = action.get('run_command')
            if run_command:
                # Replace variables with actual values
                command = run_command \
                    .replace('{{TAP}}', tap or "") \
                    .replace('{{TARGET}}', target or "") \
                    .replace('{{LOG_FILE}}', log_file or "") \
                    .replace('{{ERROR_MESSAGE}}', error_message or "") \
                    .replace('{{SCHEMA}}', schema or "") \
                    .replace('{{TABLE}}', table or "") \
                    .replace('{{DB_OBJECT}}', db_object or "") \
                    .replace('{{GRANTEE}}', grantee or "") \

                # Run command - TODO run it as a shell command not only log it
                self.logger.info("Firing {} run_command action: {}".format(event_name, command))
