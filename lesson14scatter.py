import matplotlib.pyplot as plt

countries = ['Singapore', 'Honk Kong', 'South Korea', 'Japan', 'China', 'Switzerland','Netherlands','Germany', 'Kosova', 'Albania']
iq_scores = [108, 108, 106, 105, 104, 102, 102, 101, 93, 97]

x_positions = list(range(len(countries)))

plt.figure(fissize=(10,6))
plt.scatter(x_positions, iq_scores, color="orange", s=100)
plt.title("Avarage IQ by Country (Scatter Chart)")
plt.xlabel("Country")
plt.ylabel("Avarage IQ Score")
plt.xticks(x_positions, countries, rotation = 45)
plt.grid(True)

for i, score in enumerate(iq_scores):
    plt.text(x_positions[i], score + 0.5, str(score), ha='center', va='bottom')

plt.tight_layout()
plt.show()    