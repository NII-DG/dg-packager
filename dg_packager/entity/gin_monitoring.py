from typing import Any
from nii_dg.schema.ginfork import GinMonitoring
from nii_dg.ro_crate import RootDataEntity

from dg_packager.utils.enum.property_type import PropertyType


class GinMonitoringEntity:
    def __init__(self):
        '''
        コンストラクタ
        '''

    def generate_gifork(self,
                        common_props: dict[str, Any]
                        ) -> GinMonitoring:
        '''
        Sumary
        ----------------
        ginforkのGinMonitoringEntityインスタンスの生成メソッド

        Note
        ----------------
        [param] id は 1 以上で設定してください。

        '''
        return GinMonitoring(props=common_props)

    def creata_common_props(self,
                            about: RootDataEntity,
                            contentSize: str,
                            workflowIdentifier: str,
                            datasetStructure: str,
                            experimentPackageList :list[str],
                            parameterExperimentList :list[str]
                            ) -> dict[str, Any]:
        '''
        GinMonitoringEntityの共通プロパティをdict型で取得するメソッド
        '''
        props = dict[str, Any]()

        about_id = about.data.get(PropertyType.ID.value)
        if about_id:
            props["about"] = about

        if contentSize:
            props["contentSize"] = contentSize

        if workflowIdentifier:
            props["workflowIdentifier"] = workflowIdentifier

        if datasetStructure:
            props["datasetStructure"] = datasetStructure

        if len(experimentPackageList)>0:
            props["experimentPackageList"] = experimentPackageList

        # if len(parameterExperimentList)>0:
        #     props["parameterExperimentList"] = parameterExperimentList

        return props
