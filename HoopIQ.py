import random
import calendar

class HoopIQ:
    def __init__(self):
        self.base_price = 100  # Base price for the program
        self.discount_rate = 0.1  # Discount for VIP members
        self.vip_membership_fee = 1000  # VIP membership

        #Plans and user skills
        self.skill_plans = {
            "shooting": "Improve shooting accuracy through personalized drills and shooting mechanics analysis.",
            "playmaking": "Enhance court vision and decision-making skills with tailored passing drills and game simulations.",
            "defense": "Develop defensive techniques such as footwork, anticipation, and on-ball defense through drills and film study.",
            "physicals": "Focus on strength, agility, and conditioning with a personalized workout plan tailored to individual needs."
        }
        self.player_plans = {
            "Jalen Brunson": "Learn the art of floor generalship and crafty ball-handling techniques, inspired by Jalen's style of play.",
            "LeBron James": "Study LeBron's versatility and basketball IQ, with an emphasis on leadership, playmaking, and athleticism.",
            "Kobe Bryant": "Embrace the Mamba Mentality and work on scoring techniques, footwork, and mental toughness.",
            "Nikola Jokic": "Master the fundamentals of passing, court vision, and basketball intelligence, inspired by Jokic's unique style of play.",
            "Tim Duncan": "Focus on fundamentals, discipline, and consistency in both offense and defense, mirroring Tim's legendary career."
        }
        self.live_training_plans = {
            "Dimitri": "Intensive one-on-one training sessions focusing on specific skills chosen by the participant.",
            "Devon": "Group training sessions with an emphasis on team dynamics, communication, and game scenarios."
        }

    def ask_questions(self):
        #User information for our future "database"
        print()
        print("Welcome to HoopIQ!")
        email = input("What's your email address? ")
        name = input("What's your name? ")
        location = input("Where are you located? ")
        age_group = input("How old are you? ")
        basketball_level = input("What's your basketball level (beginner/intermediate/advanced)? ")

        #Ask user if they want specific sessions
        print("\nPlease answer the following questions:")
        shooting = input("Are you interested in shooting skill development? (yes/no): ").lower() == "yes"
        playmaking = input("Are you interested in playmaking skill development? (yes/no): ").lower() == "yes"
        defense = input("Are you interested in defense skill development? (yes/no): ").lower() == "yes"
        physicals = input("Are you interested in physicals skill development? (yes/no): ").lower() == "yes"
        player_scouting = input("Are you interested in Player Scouting? (yes/no): ").lower() == "yes"
        live_training = input("Are you interested in Live Training Sessions? (yes/no): ").lower() == "yes"


        #return those answers
        return email, name, location, age_group, basketball_level, shooting, playmaking, defense, physicals, player_scouting, live_training

    def generate_plan(self, skills, player=None, live_training=None):
        #Plan for the User

        plan = ""
        for skill, interested in skills.items():
            if interested:
                if skill in self.skill_plans:
                    plan += f"\nSkill: {skill.capitalize()} - Plan: {self.skill_plans[skill]}"
                else:
                    plan += f"\nSkill: {skill.capitalize()} - Plan: Customized plan based on individual needs."

        if player:
            plan += f"\n\nPlayer Scouting - {player}: {self.player_plans[player]}"

        if live_training:
            plan += f"\n\nLive Training Session - {live_training}: {self.live_training_plans[live_training]}"

        return plan

    def calculate_price(self, skills, live_training, is_vip):
        total_price = self.base_price

        if any(skills.values()):
            total_price += 50  # Additional fee for each skill development program

        if live_training:
            total_price += 100  # Additional fee for live training sessions

        if is_vip:
            total_price += self.vip_membership_fee

        return total_price

    def generate_training_sessions(self):
        training_sessions = {}
        for month in range(5, 8):  # May to July
            month_name = calendar.month_name[month]
            session_dates = random.sample(range(1, 31), k=random.randint(3, 5))  # Randomly choose 3 to 5 dates
            training_sessions[month_name] = session_dates
        return training_sessions

    def run(self):
        email, name, location, age_group, basketball_level, shooting, playmaking, defense, physicals, player_scouting, live_training = self.ask_questions()
        player = None
        live_training_type = None

        if player_scouting:
            while True:
                print("\nChoose a player for scouting:")
                for p in self.player_plans.keys():
                    print(p)
                player = input("Enter player's name: ")
                if player in self.player_plans:
                    break
                else:
                    print("Invalid player choice. Please choose a player from the list.")

        if live_training:
            print("\nChoose a type of Live Training Session:")
            for t in self.live_training_plans.keys():
                print(t)
            live_training_type = input("Enter type of Live Training Session: ")
            if live_training_type not in self.live_training_plans:
                print("Invalid Live Training Session choice. Live Training Session will not be included.")

        plan = self.generate_plan({"shooting": shooting, "playmaking": playmaking, "defense": defense, "physicals": physicals}, player, live_training_type)
        print("\nYour personalized skill development plan:")
        print(plan)

        is_vip = input("\nWould you like to sign up for VIP membership for direct access with NBA talent? (yes/no): ").lower() == "yes"
        total_price = self.calculate_price({"shooting": shooting, "playmaking": playmaking, "defense": defense, "physicals": physicals}, live_training_type, is_vip)

        print("\n", name, ", your total monthly price for the HoopIQ program is: $", total_price)
        print("This will be emailed to ", email)

        # Generate training sessions
        training_sessions = self.generate_training_sessions()

        # Display calendar
        self.display_calendar(training_sessions)

    def display_calendar(self, training_sessions):
        for month, session_dates in training_sessions.items():
            print("\n" + month)
            for day in range(1, 31):
                if day in session_dates:
                    print(f"{day:2}: Training Session")
                else:
                    print(f"{day:2}:")

if __name__ == "__main__":
    hoop_iq = HoopIQ()
    hoop_iq.run()

    print()
    print("Thanks for choosing, HoopIQ!!")
    print()