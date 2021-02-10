import pyrebase


config = {
    "apiKey":  "AIzaSyCNzjJxfCrYn1hpLtRowCYbRplsF5ymZwo",
    "authDomain":  "go-fit-c5759.firebaseapp.com",
    "projectId":  "go-fit-c5759",
    "storageBucket":  "go-fit-c5759.appspot.com",
    "messagingSenderId":  "726214137518",
    "appId":  "1:726214137518:web:db2c322b82250a9c13ff3f",
    "measurementId": "G-FLKXJ05G49",
    "databaseURL": "https://go-fit-c5759-default-rtdb.firebaseio.com/"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()


def signIn(request):
    if request.method == POST:
        user_email = request["email"]
        user_password = request["password"]
        user = auth.sign_in_with_email_and_password(user_email, user_password)
        print(user)
        return user

    else:
        return render(request, "Login.html")


def signUp(request):
    if request.method == POST:
        user_email = request["email"]
        user_password = request["password"]
        user = auth.create_user_with_email_and_password(
            user_email, user_password)
        print(user)
        return user

    else:
        return render(request, "Register.html")


def home(request):
    return render(request, "Home.html")


def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request, "Login.html")

