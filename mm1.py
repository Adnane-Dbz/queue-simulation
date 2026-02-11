import random
import numpy as np

# Parametres
lam = 2      # taux d arrivée
mu = 3       # taux de service
N = 10000    # nombre de clients

arrival_times = []
service_times = []
start_service = []
departure_times = []

# génération des arrivees et services
t = 0
for i in range(N):
    t += random.expovariate(lam)
    arrival_times.append(t)
    service_times.append(random.expovariate(mu))

# simulation 
for i in range(N):
    if i == 0:
        start_service.append(arrival_times[i])
    else:
        start_service.append(max(arrival_times[i], departure_times[i-1]))
    departure_times.append(start_service[i] + service_times[i])

# les mesures de comprision
waiting_times = np.array(start_service) - np.array(arrival_times)
system_times = np.array(departure_times) - np.array(arrival_times)

Wq_sim = np.mean(waiting_times)
W_sim = np.mean(system_times)
rho_sim = sum(service_times) / departure_times[-1]

print("******** M/M/1 *******")
print("temps moyen d'attente Wq =", Wq_sim)
print("temps moyen dans le systeme W =", W_sim)
print("saturation du serveur ρ =", rho_sim)
print("Clients servis = 100 %")
