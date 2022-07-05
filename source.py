# STEP 1~2:GenePoolを操る
"""Provides a scripting component.
    Inputs:
        G: Input GenePool
        minimum: Set GenePool minimum
        maximum: Set GenePool maximum
        dec: Set GenePool Decimals
        cnt: Set GenePool count
        df: Set GenePool defalt
        df_update: Update defalt
        Recom: Recompute
        """

Par = ghenv.Component.Params
gp = Par.Input[0].Sources[0]

gp.Minimum = minimum
gp.Maximum = maximum
gp.Decimals = dec
gp.Count = cnt

if df_update:
    for i in range(gp.Count):
        gp.Value[i] = df

if Recom:
    gp.ExpireSolution(True)

#################################################
# STEP 3: GenePoolの指定した1パラメーターを変更

"""Provides a scripting component.
    Inputs:
        G: Input GenePool
        index: Set GenePool index
        value: Set GenePool value
        update: Update defalt & Recompute
        """

Par = ghenv.Component.Params
gp = Par.Input[0].Sources[0]

if update:
    gp.Value[index] = value
    gp.ExpireSolution(True)
