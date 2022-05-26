# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Channel Estimator MIMO 4TX
# Author: Kristian Maier, Johannes Demel
# GNU Radio version: 3.10.1.1

from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from gnuradio import lte







class lte_channel_estimator_mimo_4tx(gr.hier_block2):
    def __init__(self, N_rb_dl=50, estimator_key="slot", initial_id=333, rxant=2):
        gr.hier_block2.__init__(
            self, "Channel Estimator MIMO 4TX",
                gr.io_signature(1, 1, gr.sizeof_gr_complex*12*N_rb_dl*rxant),
                gr.io_signature.makev(4, 4, [gr.sizeof_gr_complex*12*N_rb_dl*rxant, gr.sizeof_gr_complex*12*N_rb_dl*rxant, gr.sizeof_gr_complex*12*N_rb_dl*rxant, gr.sizeof_gr_complex*12*N_rb_dl*rxant]),
        )
        self.message_port_register_hier_in("cell_id")

        ##################################################
        # Parameters
        ##################################################
        self.N_rb_dl = N_rb_dl
        self.estimator_key = estimator_key
        self.initial_id = initial_id
        self.rxant = rxant

        ##################################################
        # Variables
        ##################################################
        self.mymap3 = mymap3 = lte.frame_pilot_value_and_position(N_rb_dl, initial_id, 1, 3)
        self.mymap2 = mymap2 = lte.frame_pilot_value_and_position(N_rb_dl, initial_id, 1, 2)
        self.mymap1 = mymap1 = lte.frame_pilot_value_and_position(N_rb_dl, initial_id, 1, 1)
        self.mymap0 = mymap0 = lte.frame_pilot_value_and_position(N_rb_dl, initial_id, 1, 0)
        self.vals3 = vals3 = mymap3[1]
        self.vals2 = vals2 = mymap2[1]
        self.vals1 = vals1 = mymap1[1]
        self.vals0 = vals0 = mymap0[1]
        self.poss3 = poss3 = mymap3[0]
        self.poss2 = poss2 = mymap2[0]
        self.poss1 = poss1 = mymap1[0]
        self.poss0 = poss0 = mymap0[0]

        ##################################################
        # Blocks
        ##################################################
        self.ofdm_estimator_lte_rs_map_generator_m_1_0 = lte.rs_map_generator_m("cell_id", "pilots", N_rb_dl, 3, "$id")
        self.ofdm_estimator_lte_rs_map_generator_m_1 = lte.rs_map_generator_m("cell_id", "pilots", N_rb_dl, 1, "$id")
        self.ofdm_estimator_lte_rs_map_generator_m_0_0 = lte.rs_map_generator_m("cell_id", "pilots", N_rb_dl, 2, "$id")
        self.ofdm_estimator_lte_rs_map_generator_m_0 = lte.rs_map_generator_m("cell_id", "pilots", N_rb_dl, 0, "$id")
        self.lte_channel_estimator_vcvc_0_2 = lte.channel_estimator_vcvc(2, 12 * N_rb_dl, estimator_key, "pilots", poss3, vals3, "$id")
        self.lte_channel_estimator_vcvc_0_1 = lte.channel_estimator_vcvc(2, 12 * N_rb_dl, estimator_key, "pilots", poss2, vals2, "$id")
        self.lte_channel_estimator_vcvc_0_0 = lte.channel_estimator_vcvc(2, 12 * N_rb_dl, estimator_key, "pilots", poss1, vals1, "$id")
        self.lte_channel_estimator_vcvc_0 = lte.channel_estimator_vcvc(2, 12 * N_rb_dl, estimator_key, "pilots", poss0, vals0, "$id")


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self, 'cell_id'), (self.ofdm_estimator_lte_rs_map_generator_m_0, 'cell_id'))
        self.msg_connect((self, 'cell_id'), (self.ofdm_estimator_lte_rs_map_generator_m_0_0, 'cell_id'))
        self.msg_connect((self, 'cell_id'), (self.ofdm_estimator_lte_rs_map_generator_m_1, 'cell_id'))
        self.msg_connect((self, 'cell_id'), (self.ofdm_estimator_lte_rs_map_generator_m_1_0, 'cell_id'))
        self.msg_connect((self.ofdm_estimator_lte_rs_map_generator_m_0, 'pilots'), (self.lte_channel_estimator_vcvc_0, 'pilots'))
        self.msg_connect((self.ofdm_estimator_lte_rs_map_generator_m_0_0, 'pilots'), (self.lte_channel_estimator_vcvc_0_1, 'pilots'))
        self.msg_connect((self.ofdm_estimator_lte_rs_map_generator_m_1, 'pilots'), (self.lte_channel_estimator_vcvc_0_0, 'pilots'))
        self.msg_connect((self.ofdm_estimator_lte_rs_map_generator_m_1_0, 'pilots'), (self.lte_channel_estimator_vcvc_0_2, 'pilots'))
        self.connect((self, 0), (self.lte_channel_estimator_vcvc_0, 0))
        self.connect((self, 0), (self.lte_channel_estimator_vcvc_0_0, 0))
        self.connect((self, 0), (self.lte_channel_estimator_vcvc_0_1, 0))
        self.connect((self, 0), (self.lte_channel_estimator_vcvc_0_2, 0))
        self.connect((self.lte_channel_estimator_vcvc_0, 0), (self, 0))
        self.connect((self.lte_channel_estimator_vcvc_0_0, 0), (self, 1))
        self.connect((self.lte_channel_estimator_vcvc_0_1, 0), (self, 2))
        self.connect((self.lte_channel_estimator_vcvc_0_2, 0), (self, 3))


    def get_N_rb_dl(self):
        return self.N_rb_dl

    def set_N_rb_dl(self, N_rb_dl):
        self.N_rb_dl = N_rb_dl
        self.set_mymap0(lte.frame_pilot_value_and_position(self.N_rb_dl, self.initial_id, 1, 0))
        self.set_mymap1(lte.frame_pilot_value_and_position(self.N_rb_dl, self.initial_id, 1, 1))
        self.set_mymap2(lte.frame_pilot_value_and_position(self.N_rb_dl, self.initial_id, 1, 2))
        self.set_mymap3(lte.frame_pilot_value_and_position(self.N_rb_dl, self.initial_id, 1, 3))

    def get_estimator_key(self):
        return self.estimator_key

    def set_estimator_key(self, estimator_key):
        self.estimator_key = estimator_key

    def get_initial_id(self):
        return self.initial_id

    def set_initial_id(self, initial_id):
        self.initial_id = initial_id
        self.set_mymap0(lte.frame_pilot_value_and_position(self.N_rb_dl, self.initial_id, 1, 0))
        self.set_mymap1(lte.frame_pilot_value_and_position(self.N_rb_dl, self.initial_id, 1, 1))
        self.set_mymap2(lte.frame_pilot_value_and_position(self.N_rb_dl, self.initial_id, 1, 2))
        self.set_mymap3(lte.frame_pilot_value_and_position(self.N_rb_dl, self.initial_id, 1, 3))

    def get_rxant(self):
        return self.rxant

    def set_rxant(self, rxant):
        self.rxant = rxant

    def get_mymap3(self):
        return self.mymap3

    def set_mymap3(self, mymap3):
        self.mymap3 = mymap3
        self.set_poss3(self.mymap3[0])
        self.set_vals3(self.mymap3[1])

    def get_mymap2(self):
        return self.mymap2

    def set_mymap2(self, mymap2):
        self.mymap2 = mymap2
        self.set_poss2(self.mymap2[0])
        self.set_vals2(self.mymap2[1])

    def get_mymap1(self):
        return self.mymap1

    def set_mymap1(self, mymap1):
        self.mymap1 = mymap1
        self.set_poss1(self.mymap1[0])
        self.set_vals1(self.mymap1[1])

    def get_mymap0(self):
        return self.mymap0

    def set_mymap0(self, mymap0):
        self.mymap0 = mymap0
        self.set_poss0(self.mymap0[0])
        self.set_vals0(self.mymap0[1])

    def get_vals3(self):
        return self.vals3

    def set_vals3(self, vals3):
        self.vals3 = vals3

    def get_vals2(self):
        return self.vals2

    def set_vals2(self, vals2):
        self.vals2 = vals2

    def get_vals1(self):
        return self.vals1

    def set_vals1(self, vals1):
        self.vals1 = vals1

    def get_vals0(self):
        return self.vals0

    def set_vals0(self, vals0):
        self.vals0 = vals0

    def get_poss3(self):
        return self.poss3

    def set_poss3(self, poss3):
        self.poss3 = poss3

    def get_poss2(self):
        return self.poss2

    def set_poss2(self, poss2):
        self.poss2 = poss2

    def get_poss1(self):
        return self.poss1

    def set_poss1(self, poss1):
        self.poss1 = poss1

    def get_poss0(self):
        return self.poss0

    def set_poss0(self, poss0):
        self.poss0 = poss0

