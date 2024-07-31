import math
import matplotlib.pyplot as plt
import numpy as np


def create_noise(input_signal):
    noise = np.random.normal(0, 1, size=len(input_signal))
    signal_with_noise = noise + input_signal
    return signal_with_noise


def create_frequency_component(amplitude, n):
    f = 1 / 2
    signal = 0
    c = 0
    a = amplitude * (4 / math.pi)
    k = 1
    while c != n:
        signal += (1 / k) * np.sin(2 * k * math.pi * f * t_axis)
        k = k + 2
        c = c + 1
    signal = a * signal
    return signal


def sampling(input_signal):
    sampling_array = []
    k = int(step_range / 2)
    sampling_array.append(create_noise(input_signal)[k - 1])
    for i in range(MAX - 1):
        k = k + step_range
        sampling_array.append(create_noise(input_signal)[k])
    return sampling_array


def create_receiving_signal(sampling_array):
    signal_receiver = []
    received_bit_sequence = []
    n = 0
    for yk in sampling_array:
        if 0 < yk:
            received_bit = 0
            y_signal = +V
        else:
            received_bit = 1
            y_signal = -V
        while n != step_range:
            signal_receiver.append(y_signal)
            received_bit_sequence.append(received_bit)
            n = n + 1
        n = 0
    return signal_receiver


# first step
MAX = 5
bit_string = ""
bit = 1
i = 0
j = 0
step_range = 200
for i in range(MAX):
    if bit == 0:
        bit = 1
    elif bit == 1:
        bit = 0
    while j != step_range:
        bit_string = bit_string + str(bit)
        j = j + 1
    j = 0

# second step
V = 5
y_signal = 0
signal_sender = []
for i in range(len(bit_string)):
    if bit_string[i] == "1":
        y_signal = -V
    elif bit_string[i] == "0":
        y_signal = +V
    signal_sender.append(y_signal)
t_axis = np.arange(0, len(signal_sender) / step_range, step=1 / step_range)
first_figure = plt.figure()
plt.subplot(2, 2, 1)
# plt.ticklabel_format(style='sci', axis='x', scilimits=(1, -6))
# plt.gca().ticklabel_format(useMathText=True)
plt.plot(t_axis, signal_sender)

# third step
plt.subplot(2, 2, 2)
plt.plot(t_axis, create_noise(signal_sender))

# fourth step
sampling_result = sampling(signal_sender)

# fifth step - (part one)
plt.subplot(2, 2, 3)
plt.plot(t_axis, create_receiving_signal(sampling_result))

# fifth step - (part two)
v = 0.1
i = 0
p_axis = []
while v <= 2:
    p_axis.append((1 / 2) - ((1 / 2) * (math.erf(v) / math.sqrt(2))))
    v = v + 0.1
v_axis = np.arange(0.1, 2, step=0.1)
plt.subplot(2, 2, 4)
plt.grid(True)
plt.plot(v_axis, p_axis)

# sixth step
signal_with_two_component = create_frequency_component(V, 2)
signal_with_three_component = create_frequency_component(V, 3)
signal_with_four_component = create_frequency_component(V, 4)
second_figure = plt.figure()
plt.subplot(4, 3, 1)
plt.plot(t_axis, signal_with_two_component)
plt.subplot(4, 3, 2)
plt.plot(t_axis, signal_with_three_component)
plt.subplot(4, 3, 3)
plt.plot(t_axis, signal_with_four_component)

plt.subplot(4, 3, 4)
plt.plot(t_axis, create_noise(signal_with_two_component))
plt.subplot(4, 3, 5)
plt.plot(t_axis, create_noise(signal_with_three_component))
plt.subplot(4, 3, 6)
plt.plot(t_axis, create_noise(signal_with_four_component))

sampling_result_2 = sampling(signal_with_two_component)
sampling_result_3 = sampling(signal_with_three_component)
sampling_result_4 = sampling(signal_with_four_component)

signal_receiver_2 = create_receiving_signal(sampling_result_2)
plt.subplot(4, 3, 7)
plt.plot(t_axis, signal_receiver_2)
signal_receiver_3 = create_receiving_signal(sampling_result_3)
plt.subplot(4, 3, 8)
plt.plot(t_axis, signal_receiver_3)
signal_receiver_4 = create_receiving_signal(sampling_result_4)
plt.subplot(4, 3, 9)
plt.plot(t_axis, signal_receiver_4)

v = 0.1
i = 0
p_axis_2 = []
p_axis_3 = []
p_axis_4 = []
while v <= 2:
    p_axis_2.append(
        (1 / 2) - (1 / 2) * (math.erf(create_frequency_component(v, 2)[int(step_range / 2) - 1]) / math.sqrt(2)))
    p_axis_3.append(
        (1 / 2) - (1 / 2) * (math.erf(create_frequency_component(v, 3)[int(step_range / 2) - 1]) / math.sqrt(2)))
    p_axis_4.append(
        (1 / 2) - (1 / 2) * (math.erf(create_frequency_component(v, 4)[int(step_range / 2) - 1]) / math.sqrt(2)))
    v = v + 0.1
v_axis = np.arange(0.1, 2, step=0.1)
plt.subplot(4, 3, 11)
plt.plot(v_axis, p_axis, color="yellow", label="full signal")
plt.plot(v_axis, p_axis_2, color="blue", label="signal with 2 components")
plt.plot(v_axis, p_axis_3, color="green", label="signal with 3 components")
plt.plot(v_axis, p_axis_4, color="red", label="signal with 4 components")
plt.grid(True)
plt.legend(prop={'size': 5})

plt.show()
