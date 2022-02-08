def read_file(filepath):
    import h5py
    f = h5py.File(filepath, "r")
    color_codes, rgb, seg = f['color_codes'][:], f['rgb'][:], f['seg'][:]
    return f, color_codes, rgb, seg
# modify the file path when using
f_train, color_codes_train, rgb_train, seg_train = read_file('C:/Users/a/Desktop/mit program/assignment/team project/Lab2_train_data.h5')
f_test, color_codes_test, rgb_test, seg_test = read_file('C:/Users/a/Desktop/mit program/assignment/team project/Lab2_test_data.h5')


print(color_codes_train[:].shape)
print(rgb_train[:].shape)
print(seg_train[:].shape)

print(color_codes_test[:].shape)
print(rgb_test[:].shape)
print(seg_test[:].shape)




import matplotlib.pyplot as plt
plt.imshow(rgb_train[0][:,:,::-1])




