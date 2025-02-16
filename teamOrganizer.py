import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import random

class TeamGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("팀 생성기")
        self.root.geometry("500x650")
        self.root.configure(bg="#f0f4f8")

        self.names = []

        # 스타일 설정
        style = ttk.Style()
        style.configure("TButton", font=("Arial", 10, "bold"), padding=6)
        style.configure("TLabel", font=("Arial", 10))
        style.configure("TEntry", padding=5)

        title_label = tk.Label(root, text="🎉 랜덤 팀 생성기 🎉", font=("Arial", 18, "bold"), bg="#f0f4f8", fg="#2b2d42")
        title_label.pack(pady=10)

        # 이름 입력 프레임
        input_frame = tk.Frame(root, bg="#f0f4f8")
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="학생 이름:", font=("Arial", 10, "bold"), bg="#f0f4f8").grid(row=0, column=0, padx=5, pady=5)

        self.name_entry = ttk.Entry(input_frame, width=25, font=("Arial", 10))
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        self.name_entry.bind("<Return>", self.add_name)  # 엔터키 바인딩

        ttk.Button(input_frame, text="이름 추가", command=self.add_name).grid(row=0, column=2, padx=5, pady=5)

        # 현재 학생 명단
        tk.Label(root, text="📋 현재 학생 명단", font=("Arial", 10, "bold"), bg="#f0f4f8").pack(pady=5)
        self.name_listbox = tk.Listbox(root, width=50, height=8, font=("Arial", 9), bg="#ffffff", relief="groove", borderwidth=2)
        self.name_listbox.pack(pady=5)

        # 팀 개수 입력
        count_frame = tk.Frame(root, bg="#f0f4f8")
        count_frame.pack(pady=5)

        tk.Label(count_frame, text="팀 개수:", font=("Arial", 10, "bold"), bg="#f0f4f8").grid(row=0, column=0, padx=5)
        self.team_count_entry = ttk.Entry(count_frame, width=10, font=("Arial", 10))
        self.team_count_entry.grid(row=0, column=1, padx=5)

        # 버튼 프레임
        button_frame = tk.Frame(root, bg="#f0f4f8")
        button_frame.pack(pady=10)

        ttk.Button(button_frame, text="🎲 팀 생성", command=self.generate_teams).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(button_frame, text="🔄 다시하기", command=self.regenerate_teams).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(button_frame, text="💾 저장하기", command=self.save_to_file).grid(row=0, column=2, padx=5, pady=5)

        # 결과 표시
        tk.Label(root, text="🎉 생성된 팀 목록", font=("Arial", 10, "bold"), bg="#f0f4f8").pack(pady=5)
        self.result_text = tk.Text(root, width=60, height=12, font=("Arial", 9), wrap=tk.WORD, bg="#ffffff", relief="sunken", borderwidth=2)
        self.result_text.pack(pady=5)

    def add_name(self, event=None):
        """학생 이름을 추가 (엔터키와 버튼 공용)"""
        name = self.name_entry.get().strip()
        if name:
            self.names.append(name)
            self.name_listbox.insert(tk.END, name)
            self.name_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("경고", "이름을 입력해주세요.")

    def generate_teams(self):
        """팀을 랜덤하게 생성"""
        try:
            team_count = int(self.team_count_entry.get())
            if team_count <= 0:
                messagebox.showerror("오류", "팀 개수는 1개 이상이어야 합니다.")
                return

            if team_count > len(self.names):
                messagebox.showerror("오류", "팀 개수가 학생 수보다 많습니다.")
                return

            self.display_teams(team_count)
        except ValueError:
            messagebox.showerror("오류", "팀 개수를 숫자로 입력해주세요.")

    def regenerate_teams(self):
        """입력된 이름은 유지한 채 팀 재배정"""
        try:
            team_count = int(self.team_count_entry.get())
            if team_count <= 0:
                messagebox.showerror("오류", "팀 개수는 1개 이상이어야 합니다.")
                return

            if team_count > len(self.names):
                messagebox.showerror("오류", "팀 개수가 학생 수보다 많습니다.")
                return

            self.display_teams(team_count)
        except ValueError:
            messagebox.showerror("오류", "팀 개수를 숫자로 입력해주세요.")

    def display_teams(self, team_count):
        """팀을 화면에 표시"""
        random.shuffle(self.names)
        teams = [[] for _ in range(team_count)]

        for i, name in enumerate(self.names):
            teams[i % team_count].append(name)

        self.result_text.delete("1.0", tk.END)
        for i, team in enumerate(teams, start=1):
            self.result_text.insert(tk.END, f"✨ 팀 {i}:\n    {' , '.join(team)}\n\n")

    def save_to_file(self):
        """결과를 파일로 저장"""
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("텍스트 파일", "*.txt"), ("모든 파일", "*.*")]
        )
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.result_text.get("1.0", tk.END))
            messagebox.showinfo("저장 완료", f"파일이 {file_path}에 저장되었습니다.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TeamGeneratorApp(root)
    root.mainloop()
