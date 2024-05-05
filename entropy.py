import os
import multiprocessing
import lib.binvis as bv

test_samples = os.listdir('./sample/test')
malware_samples = os.listdir('./sample/IoT/')
benign_samples = os.listdir('./sample/IoT_benign')
cwd = os.getcwd()

out_path = '.\\out'
test_path = '.\\test'


def calc_sample_entropy(sample):
    print('[+] Calucating entropy for {}'.format(sample))
    # bv.binvis(cwd + '\\sample\\IoT\\' + sample, output_path=out_path)
    bv.binvis(cwd + '\\sample\\IoT_benign\\' + sample, output_path=out_path + '\\benign\\')
    # bv.binvis(cwd + '\\sample\\test\\' + sample, output_path=test_path)
    return


def main():
    # new_malware_samples = malware_samples.copy()
    new_benign_samples = benign_samples.copy()
    new_test_sample = test_samples.copy()
    print("[+] Benign sample size {}".format(len(new_benign_samples)))
    # for sample in new_malware_samples:
    #     if os.path.isfile(out_path + sample + '.png'):
    #         # print("[!] Sample {} already calculated skipping".format(sample))
    #         new_malware_samples.remove(sample)
    count = 0
    for sample in new_benign_samples:
        if os.path.isfile(out_path + '\\benign\\' + sample + '.png'):
            # print("[!] Sample {} already calculated skipping".format(sample))
            count += 1
            new_benign_samples.remove(sample)
    print("[!] Skiping {} samples".format(count))
    # for sample in new_test_sample:
    #    if os.path.isfile(test_path + sample + '.png'):
    #        # print("[!] Sample {} already calculated skipping".format(sample))
    #        new_test_sample.remove(sample)

    # with multiprocessing.Pool(5) as p:
    #    p.map(calc_sample_entropy, new_begin_samples)


if __name__ == "__main__":
    main()