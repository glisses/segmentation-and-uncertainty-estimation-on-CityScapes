def read_file(filepath):
    import h5py
    f = h5py.File(filepath, "r")
    color_codes, rgb, seg = f['color_codes'][:], f['rgb'][:], f['seg'][:]
    return color_codes, rgb, seg
# modify the file path when using
color_codes_train, rgb_train, seg_train = read_file('')
color_codes_test, rgb_test, seg_test = read_file('')




print(color_codes_train[:].shape)
print(rgb_train[:].shape)
print(seg_train[:].shape)

print(color_codes_test[:].shape)
print(rgb_test[:].shape)
print(seg_test[:].shape)

import matplotlib.pyplot as plt
plt.imshow(rgb_train[0][:,:,::-1])




