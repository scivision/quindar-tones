"""Simulate two-way radio in-band signaling tones"""
from __future__ import division
__version__='0.1.0'
import numpy as np
import pygame

def genquindar():
    f0 = 2525 # [Hz]  key-down tone "start PTT"
    f1 = 2475 # [Hz]  key-up tone "stop PTT"
    T = 0.25 # [s] duration of each tone is equal.
    fs = 8000 #[Hz]

    t = np.arange(0,T,1/fs)
    s0 = (np.sin(2*np.pi*f0*t)*16384).astype(np.int16)
    s1 = (np.sin(2*np.pi*f1*t)*16384).astype(np.int16)
# %%
    pygame.mixer.pre_init(fs, size=-16, channels=1, buffer=512)
    pygame.mixer.init()
    S0 = pygame.sndarray.make_sound(s0)
    S1 = pygame.sndarray.make_sound(s1)

    return S0,S1

def gentoneremote():
    # Motorola tone remote simulation
    f0 = 2175 # [Hz]
    f1 = 1950 # [Hz]
    T = 0.10 # [s]
    fs = 8000 # Hz
    t = np.arange(0,T,1/fs)

    s = np.concatenate(((np.sin(2*np.pi*f0*t)*16384).astype(np.int16),
                       (np.sin(2*np.pi*f1*t)*16384).astype(np.int16)))

# %%
    pygame.mixer.pre_init(fs, size=-16, channels=1, buffer=512)
    pygame.mixer.init()
    return pygame.sndarray.make_sound(s)


def nextel_chirp():
    """http://ttabvue.uspto.gov/ttabvue/ttabvue-91164353-OPP-77.pdf"""
    f0 = 1800 # Hz
    fs = 8000

    tbip  = np.arange(0,0.024,1/fs)
    tboop = np.arange(0,0.048,1/fs)

    bip  = (np.sin(2*np.pi*f0*tbip)*16384).astype(np.int16)
    boop = (np.sin(2*np.pi*f0*tboop)*16384).astype(np.int16)
    quiet = np.zeros_like(bip)

    s = np.concatenate((bip,quiet,bip,quiet,boop))
# %%
    pygame.mixer.pre_init(fs, size=-16, channels=1, buffer=512)
    pygame.mixer.init()
    return pygame.sndarray.make_sound(s)
