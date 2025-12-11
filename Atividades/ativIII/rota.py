class Rota:
    def __init__(self, nome: str, trecho: list[dict], delay_sinal: float):
        self.nome = nome #id da rota
        self.trecho = trecho #{"dist_km": float, "vel_kmh": float, "semaforos": int}
        self.delay_sinal = delay_sinal #atraso do semáforo em s
        
    def tempo_total_min(self) -> float:
        tempo_h = 0.0
        soma_semaforos = 0
        
        for i in self.trecho:
            tempo_h += i.get("dist_km") / i.get("vel_kmh")
            soma_semaforos += i.get("semaforos")
        
        d_m = self.delay_sinal / 60
        paradas_min = soma_semaforos * d_m
        tempo_total_min = 60 * tempo_h + paradas_min
        
        return tempo_total_min
    
    def velocidade_media_kmh(self) -> float:
        for i in self.trecho:
            distancia_total = sum(i.get("dist_km"))
            
        horas = self.tempo_total_min() / 60
        velocidade_media = distancia_total / horas
        
        return velocidade_media
    
    def atende_janela(self, inicio_min: float, fim_min: float) -> bool:
        if self.tempo_total_min() >= inicio_min and self.tempo_total_min() <= fim_min:
            return True
        return False
    
    def custo_emissao(self, kg_co2_km: float) -> float:
        for i in self.trecho:
            distancia_total = sum(i.get("dist_km"))
            
        emissao = distancia_total * kg_co2_km
        return emissao

    def __str__(self) -> str:
        return f'Rota {self.nome:<10}| Tempo: {self.tempo_total_min():.2f} min | Vel. média: {self.velocidade_media_kmh():.1f} km/h'
    
class Rota:
    def __init__(self, nome: str, trecho: list[dict], delay_sinal: float):
        self.nome = nome
        self.trecho = trecho # list[dict]
        self.delay_sinal = delay_sinal
        
    def tempo_total_min(self) -> float:
        tempo_h = 0.0
        soma_semaforos = 0
        
        for i in self.trecho:
            # Sigma (dist_km / vel_kmh)
            if i.get("vel_kmh", 0) > 0:
                tempo_h += i.get("dist_km") / i.get("vel_kmh")
            # Sigma (semaforos)
            soma_semaforos += i.get("semaforos")
            
        d_m = self.delay_sinal / 60
        paradas_min = soma_semaforos * d_m
        tempo_total_min = 60 * tempo_h + paradas_min
        
        return tempo_total_min
    
    def velocidade_media_kmh(self) -> float:
        # CORREÇÃO: Cálculo correto da distância total (Sigma dist_km)
        distancia_total = sum(t.get("dist_km") for t in self.trecho)
            
        horas = self.tempo_total_min() / 60
        
        if horas == 0:
            return 0.0
            
        velocidade_media = distancia_total / horas
        
        return velocidade_media
    
    def atende_janela(self, inicio_min: float, fim_min: float) -> bool:
        tempo = self.tempo_total_min()
        # CORREÇÃO: Usa <= e >= para incluir os limites do intervalo [início, fim]
        if tempo >= inicio_min and tempo <= fim_min:
            return True
        return False
    
    def custo_emissao(self, kg_co2_km: float) -> float:
        # CORREÇÃO: Cálculo correto da distância total (Sigma dist_km)
        distancia_total = sum(t.get("dist_km") for t in self.trecho)
            
        emissao = distancia_total * kg_co2_km
        return emissao

    def __str__(self) -> str:
        return (f'Rota {self.nome:<10}| Tempo: {self.tempo_total_min():.2f} min | '
                f'Vel. média: {self.velocidade_media_kmh():.1f} km/h')