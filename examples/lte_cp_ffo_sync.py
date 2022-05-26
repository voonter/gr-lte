# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: CP-based FFO Sync
# Author: Johannes Demel
# Description: Cyclic Prefix based synchronization for the fractional frequency offset
# GNU Radio version: 3.10.1.1

from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from gnuradio import lte







class lte_cp_ffo_sync(gr.hier_block2):
    def __init__(self, fftlen=2048):
        gr.hier_block2.__init__(
            self, "CP-based FFO Sync",
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.fftlen = fftlen

        ##################################################
        # Variables
        ##################################################
        self.cp1 = cp1 = 144 * (fftlen/2048)
        self.cp0 = cp0 = 160 * (fftlen/2048)
        self.slotl = slotl = 7 * fftlen + 6 * cp1 + cp0
        self.samp_rate = samp_rate = slotl/0.0005

        ##################################################
        # Blocks
        ##################################################
        self.sync_ffofrac_sig = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 0, 1, 0, 0)
        self.sync_ffofrac_multiply_xx_0 = blocks.multiply_vcc(1)
        self.sync_ffofrac_lte_sync_frequency_c_0 = lte.sync_frequency_c(fftlen, "$id")


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.sync_ffofrac_lte_sync_frequency_c_0, 'freq'), (self.sync_ffofrac_sig, 'cmd'))
        self.connect((self, 0), (self.sync_ffofrac_multiply_xx_0, 0))
        self.connect((self.sync_ffofrac_multiply_xx_0, 0), (self, 0))
        self.connect((self.sync_ffofrac_multiply_xx_0, 0), (self.sync_ffofrac_lte_sync_frequency_c_0, 0))
        self.connect((self.sync_ffofrac_sig, 0), (self.sync_ffofrac_multiply_xx_0, 1))


    def get_fftlen(self):
        return self.fftlen

    def set_fftlen(self, fftlen):
        self.fftlen = fftlen
        self.set_cp0(160 * (self.fftlen/2048))
        self.set_cp1(144 * (self.fftlen/2048))
        self.set_slotl(7 * self.fftlen + 6 * self.cp1 + self.cp0)

    def get_cp1(self):
        return self.cp1

    def set_cp1(self, cp1):
        self.cp1 = cp1
        self.set_slotl(7 * self.fftlen + 6 * self.cp1 + self.cp0)

    def get_cp0(self):
        return self.cp0

    def set_cp0(self, cp0):
        self.cp0 = cp0
        self.set_slotl(7 * self.fftlen + 6 * self.cp1 + self.cp0)

    def get_slotl(self):
        return self.slotl

    def set_slotl(self, slotl):
        self.slotl = slotl
        self.set_samp_rate(self.slotl/0.0005)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.sync_ffofrac_sig.set_sampling_freq(self.samp_rate)

