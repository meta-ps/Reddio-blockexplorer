import json
from pathlib import Path
import shutil
import django
import os
import sys
sys.path.append(os.getcwd())
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
django.setup()
BASE_DIR = Path(__file__).resolve().parent.parent
from django.contrib.auth.models import User

deleteRequired = True

if deleteRequired:

    path1 = Path(os.path.normpath(str(os.getcwd())+"/config/__pycache__"))
    path2 = Path(os.path.normpath(str(os.getcwd())+"/reddio/migrations"))
    path3 = Path(os.path.normpath(
        str(os.getcwd())+"/reddio/__pycache__"))
    path4 = Path(os.path.normpath(str(BASE_DIR))+"/db.sqlite3")
    path5 = Path(os.path.normpath(str(os.getcwd())+"/db.sqlite3"))

    try:
        shutil.rmtree(path1)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))

    try:
        shutil.rmtree(path2)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))

    try:
        shutil.rmtree(path3)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))

    try:
        os.remove(path5)
    except OSError as e:
        print(e)

    cmd1 = "python manage.py makemigrations"
    cmd2 = "python manage.py makemigrations reddio"
    cmd3 = "python manage.py migrate"
    username = "admin"
    email = "admin1@g.com"
    password = "kk"

    os.system(cmd1)
    os.system(cmd2)
    os.system(cmd3)
    User.objects.create_superuser(username, email, password)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")


my_data = None
with open("stark_key.json", 'r', encoding='utf-8') as f:
    my_data = json.load(f)


RECORD_BASE_API_URI = ""
DEV_NET = True
keys_length = 0
if DEV_NET:
    RECORD_BASE_API_URI = "https://api-dev.reddio.com/v1/records?stark_key="
    keys_length = 3
else:
    RECORD_BASE_API_URI = "https://api.reddio.com/v1/records?stark_key="
    keys_length = len( my_data['stark_keys'])





for i in range(keys_length):
    stark_key = my_data['stark_keys'][i]

    print(stark_key)
    RECORD_API_URI = RECORD_BASE_API_URI + stark_key

    try:
        
        print('data fetch')

    except:
        print('hlle')


# user = UserWallet()
# user.walletAddress = "0x9E08a574A85b0882e3B91db13de7854aE19B97A1"
# user.save()

# print("One User Added " + str(UserWallet.objects.all().count() == 1))


# quizz_1 = Quizz(quiz_name="Polygon Guild", user=user)
# quizz_1.save()

# question_1 = Question(question_text="Polygon Works on ?", quizz=quizz_1)
# question_1.save()

# Answer.objects.create(choice="Layer 1", is_correct=False, question=question_1)
# Answer.objects.create(choice="Layer 2", is_correct=True, question=question_1)
# Answer.objects.create(choice="Layer 3", is_correct=False, question=question_1)
# Answer.objects.create(choice="Layer 4", is_correct=False, question=question_1)

# question_2 = Question(
#     question_text="Is Polygon decentralized ?", quizz=quizz_1)
# question_2.save()

# Answer.objects.create(choice="Layer 1", is_correct=False, question=question_2)
# Answer.objects.create(choice="Layer 2", is_correct=True, question=question_2)

# # Quizz 2
# quizz_2 = Quizz(quiz_name="Polygon Guild Mumbai", user=user)
# quizz_2.save()

# question_1 = Question(question_text="ICO Full Form ?", quizz=quizz_2)
# question_1.save()

# Answer.objects.create(choice="Initial Coin Offering",
#                       is_correct=True, question=question_1)
# Answer.objects.create(choice="Initial Coin not Offering 2",
#                       is_correct=False, question=question_1)
# Answer.objects.create(choice="Initial Coin not Offering 3",
#                       is_correct=False, question=question_1)
# Answer.objects.create(choice="Initial Coin not Offering 3",
#                       is_correct=False, question=question_1)

# question_2 = Question(question_text="DAO Stands For ?", quizz=quizz_2)
# question_2.save()

# Answer.objects.create(choice="De Au org", is_correct=True, question=question_2)
# Answer.objects.create(choice="DDAS", is_correct=False, question=question_2)


# # Case 1 List all quizz Names done by user

# user = UserWallet.objects.get(walletAddress = "0x9E08a574A85b0882e3B91db13de7854aE19B97A1")
# allQuizzes = Quizz.objects.filter(user=user)
# print(allQuizzes)

# # Case 2 List all questions done by only quizz one
# quizz = Quizz.objects.get(id=1)
# questions = Question.objects.filter(quizz = quizz)
# print('All questions in a quizz')
# print(questions)
# quid = Question.objects.filter(quizz = quizz)[0]
# xx = Answer.objects.filter(question=quid)
# print(xx)

# quizz = Quizz.objects.get(id=2)
# quid2 = Question.objects.filter(quizz = quizz)[1]
# xx = Answer.objects.filter(question=quid2)
# print(xx)
