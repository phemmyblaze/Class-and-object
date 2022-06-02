class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
        print("My name is ", name, "and I am ", age, "years old.",
              "Am on the track", tracks, "and my score is", score)
        # print("My name is ", input("Enter your name: ",), "and I am ", int(input("Enter your age: ")), "years old.",
        #       "Am on the track", tracks, "and my score is", score)

    def change_name(self, new_name):
        self.name = new_name
        print(f"Changed name to {new_name}")

    def change_age(self, new_age):
        try:
            self.age = int(new_age)
        except:
            print("Age must be a number")
            raise Exception

            self.age = new_age
            print(f"Changed age to {new_age}")

    def add_track(self, new_track):
        self.tracks.append(new_track)
        print(f"Added track {new_track}")

    def get_score(self):
        return self.score


Bob = Student(name="Bob", age=26, tracks=["FE", "BE"], score=20.90)
Brenda = Student(name="Brenda", age=25, tracks=["FE", "BE"], score=15.06)


# # # Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
print(Bob.get_score())
