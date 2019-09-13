# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except ImportError:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport


class MEGAHIT(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://ci.kbase.us/services/auth/api/legacy/KBase/Sessions/Login'):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = None
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc)

    def run_megahit(self, params, context=None):
        """
        :param params: instance of type "MegaHitParams" (Run MEGAHIT.  Most
           parameters here are just passed forward to MEGAHIT workspace_name
           - the name of the workspace for input/output read_library_ref -
           the name of the PE read library (SE library support in the future)
           output_contig_set_name - the name of the output contigset
           megahit_parameter_preset - override a group of parameters;
           possible values: meta            '--min-count 2 --k-list
           21,41,61,81,99' (generic metagenomes, default) meta-sensitive 
           '--min-count 2 --k-list 21,31,41,51,61,71,81,91,99' (more
           sensitive but slower) meta-large      '--min-count 2 --k-list
           27,37,47,57,67,77,87' (large & complex metagenomes, like soil)
           bulk            '--min-count 3 --k-list 31,51,71,91,99 --no-mercy'
           (experimental, standard bulk sequencing with >= 30x depth)
           single-cell     '--min-count 3 --k-list 21,33,55,77,99,121
           --merge_level 20,0.96' (experimental, single cell data) min_count
           - minimum multiplicity for filtering (k_min+1)-mers, default 2
           min_k - minimum kmer size (<= 127), must be odd number, default 21
           max_k - maximum kmer size (<= 127), must be odd number, default 99
           k_step - increment of kmer size of each iteration (<= 28), must be
           even number, default 10 k_list - list of kmer size (all must be
           odd, in the range 15-127, increment <= 28); override `--k-min',
           `--k-max' and `--k-step' min_contig_length - minimum length of
           contigs to output, default is 2000 max_mem_percent - maximum
           memory to make available to MEGAHIT, as a percentage of available
           system memory (optional, default = 0.9 or 90%) @optional
           megahit_parameter_preset @optional min_count @optional k_min
           @optional k_max @optional k_step @optional k_list @optional
           min_contig_length @optional max_mem_percent) -> structure:
           parameter "workspace_name" of String, parameter "read_library_ref"
           of String, parameter "output_contigset_name" of String, parameter
           "megahit_parameter_preset" of String, parameter "min_count" of
           Long, parameter "k_min" of Long, parameter "k_max" of Long,
           parameter "k_step" of Long, parameter "k_list" of list of Long,
           parameter "min_contig_length" of Long, parameter "max_mem_percent"
           of Double
        :returns: instance of type "MegaHitOutput" -> structure: parameter
           "report_name" of String, parameter "report_ref" of String
        """
        return self._client.call_method('MEGAHIT.run_megahit',
                                        [params], self._service_ver, context)

    def status(self, context=None):
        return self._client.call_method('MEGAHIT.status',
                                        [], self._service_ver, context)
