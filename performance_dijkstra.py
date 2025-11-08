"""
Script para medir el rendimiento del algoritmo de Dijkstra
Ejecutar desde terminal: python performance_dijkstra.py
"""

import time
import tracemalloc
import psutil
import os
import random
from collections import deque


def distancia_minima(grafo, inicio):
    """Encuentra la distancia mínima desde un nodo inicio usando el algoritmo de Dijkstra"""
    repr = {nodo: (float('inf'), []) for nodo in grafo}
    repr[inicio] = (0, [inicio])
    no_visitados = set(grafo)

    while no_visitados:
        # Seleccionar el nodo con la distancia mínima
        nodo_min = min(no_visitados, key=lambda nodo: repr[nodo][0])
        no_visitados.remove(nodo_min)

        for conector, peso in grafo[nodo_min].items():
            if conector in no_visitados:
                nueva_distancia = repr[nodo_min][0] + peso
                if nueva_distancia < repr[conector][0]:
                    repr[conector] = (nueva_distancia, repr[nodo_min][1] + [conector])
    return repr


def medir_rendimiento(func, *args, **kwargs):
    """Función para medir tiempo de ejecución y uso de memoria"""
    
    # Iniciar medición de memoria
    tracemalloc.start()
    
    # Medir memoria del proceso antes
    process = psutil.Process(os.getpid())
    memoria_antes = process.memory_info().rss / 1024 / 1024  # MB
    
    # Medir tiempo de ejecución
    inicio = time.time()
    resultado = func(*args, **kwargs)
    fin = time.time()
    
    # Obtener el pico de uso de memoria
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    # Medir memoria del proceso después
    memoria_despues = process.memory_info().rss / 1024 / 1024  # MB
    
    estadisticas = {
        'tiempo_ejecucion': fin - inicio,
        'memoria_pico': peak / 1024 / 1024,  # MB
        'memoria_actual': current / 1024 / 1024,  # MB
        'memoria_proceso_antes': memoria_antes,
        'memoria_proceso_despues': memoria_despues,
        'diferencia_memoria_proceso': memoria_despues - memoria_antes,
        'resultado': resultado
    }
    
    return estadisticas


def generar_grafo_grande(tamaño):
    """Genera un grafo aleatorio de mayor tamaño para pruebas de rendimiento"""
    grafo_grande = {}
    
    for i in range(tamaño):
        nodo = f'N{i}'
        grafo_grande[nodo] = {}
        
        # Conectar con algunos nodos aleatorios
        num_conexiones = random.randint(1, min(5, tamaño-1))
        for _ in range(num_conexiones):
            destino = f'N{random.randint(0, tamaño-1)}'
            if destino != nodo:
                peso = random.randint(50, 500)
                grafo_grande[nodo][destino] = peso
    
    return grafo_grande


def main():
    """Función principal para ejecutar el análisis de rendimiento"""
    
    print("=" * 60)
    print("ANÁLISIS DE RENDIMIENTO - ALGORITMO DE DIJKSTRA")
    print("=" * 60)
    print()
    
    # Grafo de ejemplo
    grafo_ejemplo = {
        'A': {'B': 200, 'C': 100},
        'B': {'D': 300},
        'C': {'D': 250, 'E': 200, 'H': 300},
        'D': {'E': 100, 'F': 250},
        'E': {'G': 300},
        'F': {'G': 200},
        'H': {'G': 400},
        'G': {}
    }
    
    # 1. Prueba con grafo de ejemplo
    print("1. GRAFO DE EJEMPLO")
    print(f"   Nodos: {len(grafo_ejemplo)}")
    print(f"   Aristas: {sum(len(v) for v in grafo_ejemplo.values())}")
    print()
    
    stats_ejemplo = medir_rendimiento(distancia_minima, grafo_ejemplo, 'A')
    resultado = stats_ejemplo['resultado']
    
    print(f"   Camino A -> G: {' > '.join(resultado['G'][1])} (distancia: {resultado['G'][0]})")
    print(f"   Tiempo: {stats_ejemplo['tiempo_ejecucion']:.6f} segundos")
    print(f"   Memoria pico: {stats_ejemplo['memoria_pico']:.3f} MB")
    print(f"   Memoria actual: {stats_ejemplo['memoria_actual']:.3f} MB")
    print()
    
    # 2. Pruebas de escalabilidad
    print("-" * 60)
    print("2. ANÁLISIS DE ESCALABILIDAD")
    print("-" * 60)
    print()
    
    tamaños = [10, 25, 50, 100, 200, 500]
    resultados = []
    
    for tamaño in tamaños:
        print(f"Probando con grafo de {tamaño} nodos...")
        grafo_test = generar_grafo_grande(tamaño)
        
        stats = medir_rendimiento(distancia_minima, grafo_test, 'N0')
        
        resultados.append({
            'tamaño': tamaño,
            'tiempo': stats['tiempo_ejecucion'],
            'memoria': stats['memoria_pico']
        })
        
        print(f"   OK - Tiempo: {stats['tiempo_ejecucion']:.4f}s | Memoria: {stats['memoria_pico']:.2f} MB")
        print()
    
    # 3. Resumen estadístico
    print("=" * 60)
    print("RESUMEN ESTADÍSTICO")
    print("=" * 60)
    print()
    
    tiempo_total = sum(r['tiempo'] for r in resultados)
    tiempo_promedio = tiempo_total / len(resultados)
    memoria_promedio = sum(r['memoria'] for r in resultados) / len(resultados)
    
    print(f"Tiempo total de pruebas: {tiempo_total:.4f} segundos")
    print(f"Tiempo promedio: {tiempo_promedio:.6f} segundos")
    print(f"Memoria promedio: {memoria_promedio:.3f} MB")
    print(f"Eficiencia (tiempo × memoria): {tiempo_promedio * memoria_promedio:.6f}")
    print()
    
    # Tabla de resultados
    print("-" * 60)
    print("TABLA DE RESULTADOS DETALLADOS")
    print("-" * 60)
    print(f"{'Nodos':<10} {'Tiempo (s)':<15} {'Memoria (MB)':<15} {'Eficiencia':<15}")
    print("-" * 60)
    
    for r in resultados:
        eficiencia = r['tiempo'] * r['memoria']
        print(f"{r['tamaño']:<10} {r['tiempo']:<15.6f} {r['memoria']:<15.3f} {eficiencia:<15.6f}")
    
    print("-" * 60)
    print()
    print("Análisis completado exitosamente!")
    print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nAnálisis interrumpido por el usuario.")
    except Exception as e:
        print(f"\n\nError durante el análisis: {e}")
        import traceback
        traceback.print_exc()
