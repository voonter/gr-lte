# Copyright 2012 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
include(GrPython)

GR_PYTHON_INSTALL(PROGRAMS
    lte_bch_decoder.py
    lte_channel_estimator.py
    lte_channel_estimator_mimo_2tx.py
    lte_channel_estimator_mimo_4tx.py
    lte_cp_ffo_sync.py
    lte_cp_ffo_sync_mimo_2tx.py
    lte_ofdm_demodulator.py
    lte_ofdm_demodulator_mimo_2tx.py
    lte_pbch_decoder.py
    lte_pbch_decoder_mimo_2tx.py
    lte_pbch_decoder_mimo_4tx.py
    lte_pbch_descrambler.py
    lte_pcfich_decoder.py
    lte_pss_sync.py
    lte_pss_sync_direct_mimo_2tx.py
    lte_sss_sync.py
    lte_sss_sync_freq_domain_mimo_2tx.py
    lte_top_block_mimo_4tx.py
    lte_top_block_siso.py
    DESTINATION ${GR_PKG_LTE_EXAMPLES_DIR}
)

install(
    FILES
    lte_bch_decoder.grc
    lte_channel_estimator.grc
    lte_channel_estimator_mimo_2tx.grc
    lte_channel_estimator_mimo_4tx.grc
    lte_cp_ffo_sync.grc
    lte_cp_ffo_sync.py
    lte_cp_ffo_sync_mimo_2tx.grc
    lte_ofdm_demodulator.grc
    lte_ofdm_demodulator_mimo_2tx.grc
    lte_pbch_decoder.grc
    lte_pbch_decoder_mimo_2tx.grc
    lte_pbch_decoder_mimo_4tx.grc
    lte_pbch_descrambler.grc
    lte_pcfich_decoder.grc
    lte_pss_sync.grc
    lte_pss_sync_direct_mimo_2tx.grc
    lte_sss_sync.grc
    lte_sss_sync_freq_domain_mimo_2tx.grc
    lte_top_block_mimo_2tx.grc
    lte_top_block_mimo_4tx.grc
    lte_top_block_siso.grc
    DESTINATION ${GR_PKG_LTE_EXAMPLES_DIR}
)

