class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = list(tracks)
        self.score = score
        print("My name is ", name, "and I am ", age, "years old.",
              "Am on the track", tracks, "and my score is", score)
        # print("My name is ", input("Enter your name: ",), "and I am ", int(input("Enter your age: ")), "years old.",
        #       "Am on the track", tracks, "and my score is", score)


class Change(Student):
    def __init__(self, name, age, track, score):
        self.name = change_name
        self.age = change_age
        self.tracks = add_track
        self.score = get_score
        print("My name is ", Bob.change_name, "and I am ", Bob.change_age, "years old.",
              "Am on the track", Bob.add_track, "and my score is", Bob.get_score)
        pass


Bob = Student(name="Bob", age=26, tracks=["FE", "BE"], score=20.90)
Brenda = Student(name="Brenda", age=25, tracks=["FE", "BE"], score=15.06)


# # # Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
