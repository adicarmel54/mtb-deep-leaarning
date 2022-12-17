# from phylodeep import BD, BDEI, BDSS, FULL
# from phylodeep.checkdeep import checkdeep
# from phylodeep.modeldeep import modeldeep
# from phylodeep.paramdeep import paramdeep
import pandas as pd

cluster_count = 35
sampling_proba = 0.25
nsample = pd.read_csv('/Users/adicarmel/Desktop/nsample.txt', sep='\t')

column_names = [
    "tree_id",
    "subtree_file",
    "num_leaves",

    "prob_bd",
    "prob_bdei",
    "prob_bdss",

    "param_bd_predicted_value_R_naught",
    "param_bd_predicted_value_infectious_period",
    "param_bd_predicted_value_transmission_rate",
    "param_bd_ci_2_5_boundary_R_naught",
    "param_bd_ci_2_5_boundary_infectious_period",
    "param_bd_ci_2_5_boundary_transmission_rate",
    "param_bd_ci_97_5_boundary_R_naught",
    "param_bd_ci_97_5_boundary_infectious_period",
    "param_bd_ci_97_5_boundary_transmission_rate",

    "param_bdei_predicted_value_R_naught",
    "param_bdei_predicted_value_infectious_period",
    "param_bdei_predicted_value_incubation_period",
    "param_bdei_predicted_value_transmission_rate",
    "param_bdei_ci_2_5_boundary_R_naught",
    "param_bdei_ci_2_5_boundary_infectious_period",
    "param_bdei_ci_2_5_boundary_incubation_period",
    "param_bdei_ci_2_5_boundary_transmission_rate",
    "param_bdei_ci_97_5_boundary_R_naught",
    "param_bdei_ci_97_5_boundary_infectious_period",
    "param_bdei_ci_97_5_boundary_incubation_period",
    "param_bdei_ci_97_5_boundary_transmission_rate",

    "param_bdss_predicted_value_R_naught",
    "param_bdss_predicted_value_infectious_period",
    "param_bdss_predicted_value_X_transmission",
    "param_bdss_predicted_value_superspreading_fraction",
    "param_bdss_predicted_value_transmission_rate",
    "param_bdss_ci_2_5_boundary_R_naught",
    "param_bdss_ci_2_5_boundary_infectious_period",
    "param_bdss_ci_2_5_boundary_X_transmission",
    "param_bdss_ci_2_5_boundary_superspreading_fraction",
    "param_bdss_ci_2_5_boundary_transmission_rate",
    "param_bdss_ci_97_5_boundary_R_naught",
    "param_bdss_ci_97_5_boundary_infectious_period",
    "param_bdss_ci_97_5_X_transmission",
    "param_bdss_ci_97_5_superspreading_fraction",
    "param_bdss_ci_97_5_boundary_transmission_rate",
]
df = pd.DataFrame(columns=column_names)

for i in range(1, cluster_count + 1):
    tree_id = nsample.loc[i, "tree"]
    num_leaves = nsample.loc[i, "nsamp"]
    path_to_tree = "/data/mtb-transmission-rate-project/newick/" + tree_id + ".mcc.nwk"

    row = dict.fromkeys(column_names)
    row["tree_id"] = tree_id
    row["subtree_file"] = path_to_tree
    row["num_leaves"] = num_leaves

    if num_leaves >= 50:
        model_probs = modeldeep(path_to_tree, sampling_proba,
                                vector_representation=FULL)
        bd_params = paramdeep(path_to_tree, sampling_proba, model=BD,
                              vector_representation=FULL, ci_computation=True)
        row["prob_bd"] = model_probs.loc[0, "Probability_BD"]
        row["param_bd_predicted_value_R_naught"] = bd_params.loc["predicted_value", "R_naught"]
        row["param_bd_predicted_value_infectious_period"] = bd_params.loc["predicted_value",
                                                                          "Infectious_period"]
        row["param_bd_predicted_value_transmission_rate"] = row["param_bd_predicted_value_R_naught"] / \
            row["param_bd_predicted_value_infectious_period"]
        row["param_bd_ci_2_5_boundary_R_naught"] = bd_params.loc["ci_2_5_boundary", "R_naught"]
        row["param_bd_ci_2_5_boundary_infectious_period"] = bd_params.loc["ci_2_5_boundary",
                                                                          "Infectious_period"]
        row["param_bd_ci_2_5_boundary_transmission_rate"] = row["param_bd_ci_2_5_boundary_R_naught"] / \
            row["param_bd_ci_2_5_boundary_infectious_period"]
        row["param_bd_ci_97_5_boundary_R_naught"] = bd_params.loc["ci_97_5_boundary", "R_naught"]
        row["param_bd_ci_97_5_boundary_infectious_period"] = bd_params.loc["ci_97_5_boundary",
                                                                           "Infectious_period"]
        row["param_bd_ci_97_5_boundary_transmission_rate"] = row["param_bd_ci_97_5_boundary_R_naught"] / \
            row["param_bd_ci_97_5_boundary_infectious_period"]

        bdei_params = paramdeep(path_to_tree, sampling_proba, model=BDEI,
                                vector_representation=FULL, ci_computation=True)
        row["prob_bdei"] = model_probs.loc[0, "Probability_BDEI"]
        row["param_bdei_predicted_value_R_naught"] = bdei_params.loc["predicted_value", "R_naught"]
        row["param_bdei_predicted_value_infectious_period"] = bdei_params.loc["predicted_value", "Infectious_period"]
        row["param_bdei_predicted_value_incubation_period"] = bdei_params.loc["predicted_value", "Incubation_period"]
        row["param_bdei_predicted_value_transmission_rate"] = row["param_bdei_predicted_value_R_naught"] / \
            row["param_bdei_predicted_value_infectious_period"]
        row["param_bdei_ci_2_5_boundary_R_naught"] = bdei_params.loc["ci_2_5_boundary", "R_naught"]
        row["param_bdei_ci_2_5_boundary_infectious_period"] = bdei_params.loc["ci_2_5_boundary", "Infectious_period"]
        row["param_bdei_ci_2_5_boundary_incubation_period"] = bdei_params.loc["ci_2_5_boundary", "Incubation_period"]
        row["param_bdei_ci_2_5_boundary_transmission_rate"] = row["param_bdei_ci_2_5_boundary_R_naught"] / \
            row["param_bdei_ci_2_5_boundary_infectious_period"]
        row["param_bdei_ci_97_5_boundary_R_naught"] = bdei_params.loc["ci_97_5_boundary", "R_naught"]
        row["param_bdei_ci_97_5_boundary_infectious_period"] = bdei_params.loc["ci_97_5_boundary", "Infectious_period"]
        row["param_bdei_ci_97_5_boundary_incubation_period"] = bdei_params.loc["ci_97_5_boundary", "Incubation_period"]
        row["param_bdei_ci_97_5_boundary_transmission_rate"] = row["param_bdei_ci_97_5_boundary_R_naught"] / \
            row["param_bdei_ci_97_5_boundary_infectious_period"]

        if num_leaves >= 200:
            bdss_params = paramdeep(
                path_to_tree, sampling_proba, model=BDSS, vector_representation=FULL, ci_computation=True)
            row["prob_bdss"] = model_probs.loc[0, "Probability_BDSS"]
            row["param_bdss_predicted_value_R_naught"] = bdss_params.loc["predicted_value", "R_naught"]
            row["param_bdss_predicted_value_infectious_period"] = bdss_params.loc["predicted_value", "Infectious_period"]
            row["param_bdss_predicted_value_X_transmission"] = bdss_params.loc["predicted_value", "X_transmission"]
            row["param_bdss_predicted_value_superspreading_fraction"] = bdss_params.loc["predicted_value",
                                                                                        "Superspreading_fraction"]
            row["param_bdss_predicted_value_transmission_rate"] = row["param_bdss_predicted_value_R_naught"] / \
                row["param_bdss_predicted_value_infectious_period"]
            row["param_bdss_ci_2_5_boundary_R_naught"] = bdss_params.loc["ci_2_5_boundary", "R_naught"]
            row["param_bdss_ci_2_5_boundary_infectious_period"] = bdss_params.loc["ci_2_5_boundary", "Infectious_period"]
            row["param_bdss_ci_2_5_boundary_X_transmission"] = bdss_params.loc["ci_2_5_boundary", "X_transmission"]
            row["param_bdss_ci_2_5_boundary_superspreading_fraction"] = bdss_params.loc["ci_2_5_boundary",
                                                                                        "Superspreading_fraction"]
            row["param_bdss_ci_2_5_boundary_transmission_rate"] = row["param_bdss_ci_2_5_boundary_R_naught"] / \
                row["param_bdss_ci_2_5_boundary_infectious_period"]
            row["param_bdss_ci_97_5_boundary_R_naught"] = bdss_params.loc["ci_97_5_boundary", "R_naught"]
            row["param_bdss_ci_97_5_boundary_infectious_period"] = bdss_params.loc["ci_97_5_boundary", "Infectious_period"]
            row["param_bdss_ci_97_5_X_transmission"] = bdss_params.loc["ci_97_5_boundary", "X_transmission"]
            row["param_bdss_ci_97_5_superspreading_fraction"] = bdss_params.loc["ci_97_5_boundary",
                                                                                "Superspreading_fraction"]
            row["param_bdss_ci_97_5_boundary_transmission_rate"] = row["param_bdss_ci_97_5_boundary_R_naught"] / \
                row["param_bdss_ci_97_5_boundary_infectious_period"]

    df = df.append(row, ignore_index=True)

print(df)
