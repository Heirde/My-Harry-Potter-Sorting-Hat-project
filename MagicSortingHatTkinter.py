import tkinter as tk

class SortingHatQuiz:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("=== The Sorting Hat Quiz ===")
        self.root.geometry("400x300")
        
        # Initialize scores for each house
        self.scores = {
            "Gryffindor": 0,
            "Hufflepuff": 0,
            "Slytherin": 0,
            "Ravenclaw": 0
        }
        
        # Question counter
        self.current_question = 0
        self.questions = [
            "What House are you?",
            "What quality do you value most?",
            "Which magical creature appeals to you?",
            "What would you most like to be remembered as?",
            "What's your greatest fear?"
        ]
        
        # Create UI elements
        self.create_widgets()
        self.show_question()
    
    def create_widgets(self):
        # Question label
        self.question_label = tk.Label(self.root, text="", font=("Arial", 12), wraplength=350)
        self.question_label.pack(pady=20)
        
        # House buttons
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)
        
        self.gryffindor_btn = tk.Button(self.button_frame, text="Gryffindor", 
                                       command=lambda: self.add_score("Gryffindor"),
                                       width=12, bg="#7d0000", fg="white")
        self.gryffindor_btn.pack(pady=5)
        
        self.hufflepuff_btn = tk.Button(self.button_frame, text="Hufflepuff", 
                                       command=lambda: self.add_score("Hufflepuff"),
                                       width=12, bg="#ffdb00", fg="black")
        self.hufflepuff_btn.pack(pady=5)
        
        self.slytherin_btn = tk.Button(self.button_frame, text="Slytherin", 
                                      command=lambda: self.add_score("Slytherin"),
                                      width=12, bg="#0d4d0d", fg="white")
        self.slytherin_btn.pack(pady=5)
        
        self.ravenclaw_btn = tk.Button(self.button_frame, text="Ravenclaw", 
                                      command=lambda: self.add_score("Ravenclaw"),
                                      width=12, bg="#0d47a1", fg="white")
        self.ravenclaw_btn.pack(pady=5)
        
        # Score display
        self.score_label = tk.Label(self.root, text="", font=("Arial", 10))
        self.score_label.pack(pady=10)
        
        # Reset button
        self.reset_btn = tk.Button(self.root, text="Reset Quiz", command=self.reset_quiz)
        self.reset_btn.pack(pady=5)
    
    def show_question(self):
        if self.current_question < len(self.questions):
            question_text = f"Q{self.current_question + 1}) {self.questions[self.current_question]}"
            self.question_label.config(text=question_text)
            self.update_button_text()
        else:
            self.show_final_result()
    
    def update_button_text(self):
        # Change button text based on current question
        question_responses = [
            # Q1: What House are you?
            ["Gryffindor", "Hufflepuff", "Slytherin", "Ravenclaw"],
            # Q2: What quality do you value most?
            ["Bravery", "Loyalty", "Ambition", "Wisdom"],
            # Q3: Which magical creature appeals to you?
            ["Phoenix", "Badger", "Snake", "Eagle"],
            # Q4: What would you most like to be remembered as?
            ["The Bold", "The Kind", "The Great", "The Wise"],
            # Q5: What's your greatest fear?
            ["Cowardice", "Isolation", "Failure", "Ignorance"]
        ]
        
        if self.current_question < len(question_responses):
            responses = question_responses[self.current_question]
            self.gryffindor_btn.config(text=responses[0])
            self.hufflepuff_btn.config(text=responses[1])
            self.slytherin_btn.config(text=responses[2])
            self.ravenclaw_btn.config(text=responses[3])
    
    def add_score(self, house):
        self.scores[house] += 1
        self.current_question += 1
        self.update_score_display()
        self.show_question()
    
    def update_score_display(self):
        score_text = "Current Scores: "
        score_parts = []
        for house, score in self.scores.items():
            score_parts.append(f"{house}: {score}")
        score_text += " | ".join(score_parts)
        self.score_label.config(text=score_text)
    
    def show_final_result(self):
        # Find the house with the highest score
        max_score = max(self.scores.values())
        winning_houses = []
        for house_name, house_score in self.scores.items():
            if house_score == max_score:
                winning_houses.append(house_name)
        
        if len(winning_houses) == 1:
            result_text = f"🎉 Congratulations! You belong in {winning_houses[0]}! 🎉"
        else:
            result_text = f"It's a tie between: {', '.join(winning_houses)}!\nYou have qualities of multiple houses!"
        
        self.question_label.config(text=result_text)
        
        # Hide the house buttons
        self.gryffindor_btn.pack_forget()
        self.hufflepuff_btn.pack_forget()
        self.slytherin_btn.pack_forget()
        self.ravenclaw_btn.pack_forget()
        
        # Show final scores
        final_score_text = "Final Scores:\n"
        # Sort houses by score (highest first)
        sorted_scores = sorted(self.scores.items(), key=lambda item: item[1], reverse=True)
        for house_name, house_score in sorted_scores:
            final_score_text += f"{house_name}: {house_score}\n"
        
        self.final_label = tk.Label(self.root, text=final_score_text, font=("Arial", 10))
        self.final_label.pack(pady=10)

    def reset_quiz(self):

        self.scores = {house: 0 for house in self.scores}
        self.current_question

        if hasattr(self, "final_label"):
            self.final_label.destroy()

        self.gryffindor_btn.pack(pady=5)
        self.hufflepuff_btn.pack(pady=5)
        self.slytherin_btn.pack(pady=5)
        self.ravenclaw_btn.pack(pady=5)

        self.update_score_display()
        self.show_question()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    quiz = SortingHatQuiz()
    quiz.run()
            