import pandas as pd
import matplotlib.pyplot as plt

def plot_memory_usage(log_file):
    df = pd.read_csv(log_file)
    
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    
    df['Used Memory (GB)'] = df['Used Memory (KB)'] / (1024 * 1024)
    
    plt.figure(figsize=(12, 6))
    plt.plot(df['Timestamp'], df['Used Memory (GB)'], marker='o', linestyle='-', color='b')
    plt.title('Memory Usage Over Time')
    plt.xlabel('Timestamp')
    plt.ylabel('Memory Usage (GB)')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()  
    plt.savefig('memory_usage_plot.png') 
    plt.show()

if __name__ == "__main__":
    log_file = 'memory_usage.log'
    plot_memory_usage(log_file)