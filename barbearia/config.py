class Config(object):
    SECRET_KEY = '03c67c676b4fcf005bee69ae'
    SQLALCHEMY_DATABASE_URI='postgresql://nawtnucbclasnz:3011841ec78eb8824ffa194f91af7e3b8ebdfce225518de9a7161190186ddf3c@ec2-44-195-201-3.compute-1.amazonaws.com:5432/d26chn0b080oo9'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOGIN_DISABLED = True         #usar apenas durante periodo de desenvolvimento