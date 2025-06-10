import matplotlib.pyplot as plt

countries = ['Singapore', 'Honk Kong', 'South Korea', 'Japan', 'China', 'Switzerland','Netherlands','Germany', 'Kosova', 'Albania']
iq_scores = [108, 108, 106, 105, 104, 102, 102, 101, 93, 97]

plt.figure(figsize=(10,6))
plt.plot(countries, iq_scores, marker='o', linestyle='-',linewidth=2)

plt.title("Avarage IQ by Line Chart, va='bottom")
plt.xlabel("Country")
plt.ylabel("Avarage IQ Score")
plt.xticks(rotation = 45)
plt.grid(True)

for i, score in enumerate(iq_scores):
    plt.text(countries[i], score + 0.5, str(score), ha='center', va='bottom')
    
plt.tight_layout()
plt.show()