import random
import numpy as np

# Paramètres
lam = 4      # taux d'arrivée
mu = 3       # taux de service
c = 2        # nombre de serveurs
N = 10000

arrival_times = []
service_times = []
server_free_time = [0] * c
start_service = []
departure_times = []

# génération des arrivées
t = 0
for i in range(N):
    t += random.expovariate(lam)
    arrival_times.append(t)
    service_times.append(random.expovariate(mu))

# simulation
for i in range(N):
    server_index = np.argmin(server_free_time)
    start = max(arrival_times[i], server_free_time[server_index])
    end = start + service_times[i]

    server_free_time[server_index] = end
    start_service.append(start)
    departure_times.append(end)

# Mesures
waiting_times = np.array(start_service) - np.array(arrival_times)
system_times = np.array(departure_times) - np.array(arrival_times)

Wq_sim = np.mean(waiting_times)
W_sim = np.mean(system_times)
rho_sim = sum(service_times) / (c * departure_times[-1])

print("=== M/M/c ===")
print("Temps moyen d'attente Wq =", Wq_sim)
print("Temps moyen dans le système W =", W_sim)
print("Saturation moyenne ρ =", rho_sim)
print("Clients servis = 100 %")
