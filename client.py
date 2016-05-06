from xivo_amid_client import Client

c = Client('dev', token='e26b124d-ea4b-5308-a243-803352c14bc9')

print c.action('DBGet', {'Family': 'PWET', 'Key': 'Pwet'})
