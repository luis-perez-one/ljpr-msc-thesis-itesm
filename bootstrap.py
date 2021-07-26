import numpy as np 

def single_bsample(data):
    n = data.size
    # random positions vector
    i_vector = np.random.randint(n, size=n).tolist()
    boot_sample = [data[i] for i in i_vector]
    boot_sample = np.array(boot_sample)
    return boot_sample

def multi_bsamples(data, n):
    boot_samples = np.ones(n).tolist()
    boot_samples = [single_bsample(data)*s for s in boot_samples]
    return boot_samples


x = np.array([24,13,12,10.52,11,9.34,13.1,12.7,14.1])
x_boot_samples = multi_bsamples(x,2000)
x_boot_samples_mean = [*map(lambda s: s.mean(), x_boot_samples)]
x_boot_samples_mean = np.array(x_boot_samples_mean)
boot_punctual = x_boot_samples_mean.mean()
boot_standard_error = x_boot_samples_mean.std()
p05 = np.percentile(x_boot_samples_mean, 5)
p95 = np.percentile(x_boot_samples_mean, 95)



print(boot_punctual, boot_standard_error, p05, p95)


    


