# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: PSS-based CP Sync MIMO 2TX
# Author: Kristian Maier
# GNU Radio version: 3.10.1.1

from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from gnuradio import lte







class lte_cp_ffo_sync_mimo_2tx(gr.hier_block2):
    def __init__(self, fftlen=1024, rxant=2):
        gr.hier_block2.__init__(
            self, "PSS-based CP Sync MIMO 2TX",
                gr.io_signature.makev(2, 2, [gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1]),
                gr.io_signature.makev(2, 2, [gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1]),
        )

        ##################################################
        # Parameters
        ##################################################
        self.fftlen = fftlen
        self.rxant = rxant

        ##################################################
        # Blocks
        ##################################################
        self.sync_ffofrac_sig = analog.sig_source_c(fftlen*15e3, analog.GR_SIN_WAVE, 0, 1, 0, 0)
        self.lte_mimo_pss_freq_sync_0 = lte.mimo_pss_freq_sync(fftlen,rxant,self."sync_ffofrac_sig")
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.lte_mimo_pss_freq_sync_0, 'freq'), (self.sync_ffofrac_sig, 'cmd'))
        self.connect((self.blocks_multiply_xx_0, 0), (self.lte_mimo_pss_freq_sync_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.lte_mimo_pss_freq_sync_0, 1))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self, 1))
        self.connect((self, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self, 1), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.sync_ffofrac_sig, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.sync_ffofrac_sig, 0), (self.blocks_multiply_xx_0_0, 1))


    def get_fftlen(self):
        return self.fftlen

    def set_fftlen(self, fftlen):
        self.fftlen = fftlen
        self.sync_ffofrac_sig.set_sampling_freq(self.fftlen*15e3)

    def get_rxant(self):
        return self.rxant

    def set_rxant(self, rxant):
        self.rxant = rxant

