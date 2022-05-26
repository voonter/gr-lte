# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Channel Estimator
# Author: Johannes Demel
# Description: hierarchical block containing all parts of a linear LTE estimator
# GNU Radio version: 3.10.1.1

from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from gnuradio import lte







class lte_channel_estimator(gr.hier_block2):
    def __init__(self, N_rb_dl=50, estimator_key="slot", initial_id=0):
        gr.hier_block2.__init__(
            self, "Channel Estimator",
                gr.io_signature(1, 1, gr.sizeof_gr_complex*12*N_rb_dl),
                gr.io_signature.makev(2, 2, [gr.sizeof_gr_complex*12*N_rb_dl, gr.sizeof_gr_complex*12*N_rb_dl]),
        )
        self.message_port_register_hier_in("cell_id")

        ##################################################
        # Parameters
        ##################################################
        self.N_rb_dl = N_rb_dl
        self.estimator_key = estimator_key
        self.initial_id = initial_id

        ##################################################
        # Variables
        ##################################################
        self.mymap1 = mymap1 = lte.frame_pilot_value_and_position(N_rb_dl, initial_id, 1, 0)
        self.mymap = mymap = lte.frame_pilot_value_and_position(N_rb_dl, initial_id, 1, 0)
        self.vals = vals = mymap[1]
        self.poss1 = poss1 = mymap1[0]
        self.poss0 = poss0 = mymap[0]

        ##################################################
        # Blocks
        ##################################################
        self.ofdm_estimator_lte_rs_map_generator_m_1 = lte.rs_map_generator_m("cell_id", "pilots", N_rb_dl, 1, "$id")
        self.ofdm_estimator_lte_rs_map_generator_m_0 = lte.rs_map_generator_m("cell_id", "pilots", N_rb_dl, 0, "$id")
        self.lte_channel_estimator_vcvc_0_0 = lte.channel_estimator_vcvc(1, 12*N_rb_dl, estimator_key, "pilots", poss1, vals, "$id")
        self.lte_channel_estimator_vcvc_0 = lte.channel_estimator_vcvc(1, 12*N_rb_dl, estimator_key, "pilots", poss0, vals, "$id")


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self, 'cell_id'), (self.ofdm_estimator_lte_rs_map_generator_m_0, 'cell_id'))
        self.msg_connect((self, 'cell_id'), (self.ofdm_estimator_lte_rs_map_generator_m_1, 'cell_id'))
        self.msg_connect((self.ofdm_estimator_lte_rs_map_generator_m_0, 'pilots'), (self.lte_channel_estimator_vcvc_0, 'pilots'))
        self.msg_connect((self.ofdm_estimator_lte_rs_map_generator_m_1, 'pilots'), (self.lte_channel_estimator_vcvc_0_0, 'pilots'))
        self.connect((self, 0), (self.lte_channel_estimator_vcvc_0, 0))
        self.connect((self, 0), (self.lte_channel_estimator_vcvc_0_0, 0))
        self.connect((self.lte_channel_estimator_vcvc_0, 0), (self, 0))
        self.connect((self.lte_channel_estimator_vcvc_0_0, 0), (self, 1))


    def get_N_rb_dl(self):
        return self.N_rb_dl

    def set_N_rb_dl(self, N_rb_dl):
        self.N_rb_dl = N_rb_dl
        self.set_mymap(lte.frame_pilot_value_and_position(self.N_rb_dl, self.initial_id, 1, 0))
        self.set_mymap1(lte.frame_pilot_value_and_position(self.N_rb_dl, self.initial_id, 1, 0))

    def get_estimator_key(self):
        return self.estimator_key

    def set_estimator_key(self, estimator_key):
        self.estimator_key = estimator_key

    def get_initial_id(self):
        return self.initial_id

    def set_initial_id(self, initial_id):
        self.initial_id = initial_id
        self.set_mymap(lte.frame_pilot_value_and_position(self.N_rb_dl, self.initial_id, 1, 0))
        self.set_mymap1(lte.frame_pilot_value_and_position(self.N_rb_dl, self.initial_id, 1, 0))

    def get_mymap1(self):
        return self.mymap1

    def set_mymap1(self, mymap1):
        self.mymap1 = mymap1
        self.set_poss1(self.mymap1[0])

    def get_mymap(self):
        return self.mymap

    def set_mymap(self, mymap):
        self.mymap = mymap
        self.set_poss0(self.mymap[0])
        self.set_vals(self.mymap[1])

    def get_vals(self):
        return self.vals

    def set_vals(self, vals):
        self.vals = vals

    def get_poss1(self):
        return self.poss1

    def set_poss1(self, poss1):
        self.poss1 = poss1

    def get_poss0(self):
        return self.poss0

    def set_poss0(self, poss0):
        self.poss0 = poss0

