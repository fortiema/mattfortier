Title: Setting Up an Nvidia GPU with Tensorflow in Fedora/RHEL/CentOS
Date: 2017-01-09 9:00
Tags: guide gpu cuda fedora tensorflow
Category: Guides
Slug: nvidia-cuda-tensorflow-fedora-guide

2017 is upon us and I have the feeling many of you have taken the resolution this year to finally get your feet wet with Deep Learning and AI. You've bought yourself a nice Nvidia Pascal GPU and are getting ready to put that beast to good use. I fall in this category, and went through the relatively small trouble of installing my new GTX1060 on a fresh Fedora 25 build.

If you already have a RHEL-based setup, or are maybe looking at the new Fedora 25 release as a potential good host, follow along for a smooth experience in getting everything ready.

## 1. Add Negativo17's fedora-nvidia Repo

Nvidia's official repo is a little bit out of touch with current developements in the Red Hat distribution world, and is a little bit messy. This is where [negativo17 repo](http://negativo17.org/nvidia-driver/), with its excellent repackaging of Nvidia librairies, comes into play and makes everything much simpler. Let's add the repo to our installation:

_Fedora_

```python
dnf config-manager --add-repo=http://negativo17.org/repos/fedora-nvidia.repo
```

_RHEL/CentOS_

```python
yum-config-manager --add-repo=http://negativo17.org/repos/epel-nvidia.repo
```

Fedora 25 has support for the packages directly in Gnome Software, so this can make your life even easier if you wish to go that route.

## 2. Install Necessary Packages

One of the big diffenrences in Negativo17's repository is that packages and subpackages are better separated. This means you have more granular control over which librairies/drivers you install. For more info, and if you have specefic needs in terms of packages you want/need, you can refer to the [repository explanation page](http://negativo17.org/nvidia-driver/).

Although you could install every package in a single command, I prefer to install the CUDA libraries first, and then install all the drivers and utilities.

_Fedora_

```python
dnf install cuda cuda-devel cuda-cudnn*

dnf install nvidia-settings kernel-devel dkms-nvidia vulkan.i686 nvidia-driver-libs.i686 nvidia-driver-cuda
```

_RHEL/CentOS_

> RHEL and CentOS currently do not offer Vulkan support. This could change in the future.

```python
yum install cuda cuda-devel cuda-cudnn*

yum install nvidia-settings kernel-devel dkms-nvidia nvidia-driver-libs.i686 nvidia-driver-cuda
```

Once done, reboot your machine.

## 3. Setup Tensorflow-GPU

> Tensorflow v0.12.1 was the latest version at the time of writing this post

You now need to install the version of Tensorflow with GPU support. I recommend you install TF in a virtualenv for convenience and safety so go ahead and do that. Once activated you can proceed with the install:

```python
# Store the TF wheel URL into a var for convenience
export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-0.12.1-cp27-none-linux_x86_64.whl

#Install using pip (you can drop the '--upgrade' if it's a fresh install):
pip install --upgrade $TF_BINARY_URL
```

## 4. Test Your Setup

You're ready to test! Let's write a simple matrix multiplication script and execute it. I suggest you run it line-by-line in your Python REPL to benefit from the verbrosity.

```python
import tensorflow as tf
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))

a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
c = tf.matmul(a, b)
print sess.run(c)
```

If everything is right, you'll see an output resembling this one:

```python
Python 2.7.13 (default, Jan  8 2017, 15:53:39)
[GCC 6.3.1 20161221 (Red Hat 6.3.1-1)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import tensorflow as tf
I tensorflow/stream_executor/dso_loader.cc:128] successfully opened CUDA library libcublas.so locally
I tensorflow/stream_executor/dso_loader.cc:128] successfully opened CUDA library libcudnn.so locally
I tensorflow/stream_executor/dso_loader.cc:128] successfully opened CUDA library libcufft.so locally
I tensorflow/stream_executor/dso_loader.cc:128] successfully opened CUDA library libcuda.so.1 locally
I tensorflow/stream_executor/dso_loader.cc:128] successfully opened CUDA library libcurand.so locally
>>> sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
I tensorflow/core/common_runtime/gpu/gpu_device.cc:885] Found device 0 with properties:
name: GeForce GTX 1060 6GB
major: 6 minor: 1 memoryClockRate (GHz) 1.759
pciBusID 0000:01:00.0
Total memory: 5.93GiB
Free memory: 5.64GiB
I tensorflow/core/common_runtime/gpu/gpu_device.cc:906] DMA: 0
I tensorflow/core/common_runtime/gpu/gpu_device.cc:916] 0:   Y
I tensorflow/core/common_runtime/gpu/gpu_device.cc:975] Creating TensorFlow device (/gpu:0) -> (device: 0, name: GeForce GTX 1060 6GB, pci bus id: 0000:01:00.0)
Device mapping:
/job:localhost/replica:0/task:0/gpu:0 -> device: 0, name: GeForce GTX 1060 6GB, pci bus id: 0000:01:00.0
I tensorflow/core/common_runtime/direct_session.cc:255] Device mapping:
/job:localhost/replica:0/task:0/gpu:0 -> device: 0, name: GeForce GTX 1060 6GB, pci bus id: 0000:01:00.0

>>> a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
>>> b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
>>> c = tf.matmul(a, b)
>>> print sess.run(c)
MatMul: (MatMul): /job:localhost/replica:0/task:0/gpu:0
I tensorflow/core/common_runtime/simple_placer.cc:827] MatMul: (MatMul)/job:localhost/replica:0/task:0/gpu:0
b: (Const): /job:localhost/replica:0/task:0/gpu:0
I tensorflow/core/common_runtime/simple_placer.cc:827] b: (Const)/job:localhost/replica:0/task:0/gpu:0
a: (Const): /job:localhost/replica:0/task:0/gpu:0
I tensorflow/core/common_runtime/simple_placer.cc:827] a: (Const)/job:localhost/replica:0/task:0/gpu:0
[[ 22.  28.]
 [ 49.  64.]]
```

That's it, you're ready to put all these Watts to good use!
