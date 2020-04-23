
import uuid

class TestConstraints:
    userName = 'pvpsuman'
    password = 'testpassword{}'.format(uuid.uuid4().hex[:5])
    email = 'pvpsuman@gmail.com'