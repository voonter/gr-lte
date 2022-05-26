# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: PSS Sync direct MIMO 2TX
# Author: Kristian Maier
# GNU Radio version: 3.10.1.1

from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from gnuradio import lte







class lte_pss_sync_direct_mimo_2tx(gr.hier_block2):
    def __init__(self, fftlen=2048, rxant=2, synclen=4):
        gr.hier_block2.__init__(
            self, "PSS Sync direct MIMO 2TX",
                gr.io_signature.makev(2, 2, [gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1]),
                gr.io_signature.makev(2, 2, [gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1]),
        )
        self.message_port_register_hier_out("N_id_2")

        ##################################################
        # Parameters
        ##################################################
        self.fftlen = fftlen
        self.rxant = rxant
        self.synclen = synclen

        ##################################################
        # Variables
        ##################################################
        self.taps = taps = filter.optfir.low_pass(1, fftlen*15e3, 472.5e3, 900e3, 0.2, 40)

        ##################################################
        # Blocks
        ##################################################
        self.lte_mimo_pss_tagger_0 = lte.mimo_pss_tagger(fftlen)
        self.lte_mimo_pss_fine_sync_1 = lte.mimo_pss_fine_sync(fftlen, rxant, len(taps)//2)
        self.lte_mimo_pss_coarse_sync_0 = lte.mimo_pss_coarse_sync(synclen, rxant)
        self.lte_mimo_pss_coarse_control_0 = lte.mimo_pss_coarse_control(rxant)
        self.fir_filter_xxx_0_0 = filter.fir_filter_ccc(fftlen//64, taps)
        self.fir_filter_xxx_0_0.declare_sample_delay(0)
        self.fir_filter_xxx_0 = filter.fir_filter_ccc(fftlen//64, taps)
        self.fir_filter_xxx_0.declare_sample_delay(0)


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.lte_mimo_pss_coarse_sync_0, 'control'), (self.lte_mimo_pss_coarse_control_0, 'control'))
        self.msg_connect((self.lte_mimo_pss_coarse_sync_0, 'coarse_pos'), (self.lte_mimo_pss_fine_sync_1, 'coarse_pos'))
        self.msg_connect((self.lte_mimo_pss_coarse_sync_0, 'N_id_2'), (self.lte_mimo_pss_fine_sync_1, 'N_id_2'))
        self.msg_connect((self.lte_mimo_pss_coarse_sync_0, 'N_id_2'), (self.lte_mimo_pss_tagger_0, 'N_id_2'))
        self.msg_connect((self.lte_mimo_pss_coarse_sync_0, 'N_id_2'), (self, 'N_id_2'))
        self.msg_connect((self.lte_mimo_pss_fine_sync_1, 'half_frame'), (self.lte_mimo_pss_tagger_0, 'half_frame'))
        self.msg_connect((self.lte_mimo_pss_fine_sync_1, 'lock'), (self.lte_mimo_pss_tagger_0, 'lock'))
        self.connect((self.fir_filter_xxx_0, 0), (self.lte_mimo_pss_coarse_sync_0, 0))
        self.connect((self.fir_filter_xxx_0_0, 0), (self.lte_mimo_pss_coarse_sync_0, 1))
        self.connect((self.lte_mimo_pss_coarse_control_0, 0), (self.fir_filter_xxx_0, 0))
        self.connect((self.lte_mimo_pss_coarse_control_0, 1), (self.fir_filter_xxx_0_0, 0))
        self.connect((self.lte_mimo_pss_tagger_0, 1), (self, 1))
        self.connect((self.lte_mimo_pss_tagger_0, 0), (self, 0))
        self.connect((self, 1), (self.lte_mimo_pss_coarse_control_0, 1))
        self.connect((self, 0), (self.lte_mimo_pss_coarse_control_0, 0))
        self.connect((self, 1), (self.lte_mimo_pss_fine_sync_1, 1))
        self.connect((self, 0), (self.lte_mimo_pss_fine_sync_1, 0))
        self.connect((self, 1), (self.lte_mimo_pss_tagger_0, 1))
        self.connect((self, 0), (self.lte_mimo_pss_tagger_0, 0))


    def get_fftlen(self):
        return self.fftlen

    def set_fftlen(self, fftlen):
        self.fftlen = fftlen
        self.set_taps(filter.optfir.low_pass(1, self.fftlen*15e3, 472.5e3, 900e3, 0.2, 40))

    def get_rxant(self):
        return self.rxant

    def set_rxant(self, rxant):
        self.rxant = rxant

    def get_synclen(self):
        return self.synclen

    def set_synclen(self, synclen):
        self.synclen = synclen

    def get_taps(self):
        return self.taps

    def set_taps(self, taps):
        self.taps = taps
        self.fir_filter_xxx_0.set_taps(self.taps)
        self.fir_filter_xxx_0_0.set_taps(self.taps)

