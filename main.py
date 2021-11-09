import discord
import datetime

client = discord.Client()

def log(*lines):
    print(datetime.datetime.now().isoformat(), *lines)

events = [
        ('on_connect', []),
        ('on_shard_connect', ['shard_id']),
        ('on_disconnect', []),
        ('on_shard_disconnect', ['shard_id']),
        ('on_ready', []),
        ('on_shard_ready', ['shard_id']),
        ('on_resumed', []),
        ('on_shard_resumed', ['shard_id']),
        ('on_error', ['event']),
        ('on_socket_raw_receive', ['msg']),
        ('on_socket_raw_send', ['msg']),
        ('on_typing', ['channel', 'user', 'when']),

        ('on_message', ['message']),
        ('on_message_delete', ['message']),
        ('on_bulk_message_delete', ['messages']),
        ('on_raw_message_delete', ['payload']),
        ('on_raw_bulk_message_delete', ['payload']),
        ('on_message_edit', ['before', 'after']),
        ('on_raw_message_edit', ['payload']),
        ('on_reaction_add', ['reaction', 'user']),
        ('on_raw_reaction_add', ['payload']),
        ('on_reaction_remove', ['reaction', 'user']),
        ('on_raw_reaction_remove', ['payload']),
        ('on_reaction_clear', ['message', 'reactions']),
        ('on_raw_reaction_clear', ['payload']),
        ('on_reaction_clear_emoji', ['reaction']),
        ('on_raw_reaction_clear_emoji', ['payload']),

        ('on_private_channel_delete', ['channel']),
        ('on_private_channel_create', ['channel']),
        ('on_private_channel_update', ['before', 'after']),
        ('on_private_channel_pins_update', ['channel', 'last_pin']),
        ('on_guild_channel_delete', ['channel']),
        ('on_guild_channel_create', ['channel']),
        ('on_guild_channel_update', ['before', 'after']),
        ('on_guild_channel_pins_update', ['channel', 'last_pin']),

        ('on_guild_interactions_update', ['guild']),
        ('on_webhooks_update', ['channel']),

        ('on_member_join', ['member']),
        ('on_member_leave', ['member']),
        ('on_member_update', ['before', 'after']),
        ('on_user_update', ['before', 'after']),
        
        ('on_guild_join', ['guild']),
        ('on_guild_remove', ['guild']),
        ('on_guild_update', ['before', 'after']),
        ('on_guild_role_create', ['role']),
        ('on_guild_role_delete', ['role']),
        ('on_guild_role_update', ['before', 'after']),
        ('on_guild_emojis_update', ['guild', 'before', 'after']),
        ('on_guild_available', ['guild']),
        ('on_guild_unavailable', ['guild']),

        ('on_voice_state_change', ['member', 'before', 'after']),
        ('on_member_ban', ['guild', 'user']),
        ('on_member_unban', ['guild', 'user']),

        ('on_invite_create', ['invite']),
        ('on_invite_delete', ['invite']),

        ('on_group_join', ['channel', 'user']),
        ('on_group_remove', ['channel', 'user']),

        ('on_relationship_add', ['relationship']),
        ('on_relationship_remove', ['relationship']),
        ('on_relationship_update', ['before', 'after']),
]

for name, target_args in events:
    async def ev(*args, __name=name, __target_args=target_args, **kwargs):
        arg_lines = []
        if args: arg_lines.append('')
        for i in range(len(args)):
            try:
                arg_lines.append(f"\t{__target_args[i]}={repr(args[i])},")
            except IndexError:
                arg_lines.append(f"\t{repr(args[i])},")

        for key in kwargs:
            arg_lines.append(f"\t{key}={repr(kwargs[key])},")

        if args: arg_lines.append('')

        log_line = f"{__name}(" + '\n'.join(arg_lines) + ')'
        log(log_line)

    setattr(client, name, ev)

client.run(input("TOKEN: "))
