import os
import itertools
import random

if __name__ == '__main__':
    epochs = 200
    flow_crits = ['epe']
    t_crits = ['partial_rms']
    rot_crit = ['quat_product_1']
    rot_factors = [1]
    flow_factors = [15]
    target_factors = [0.5]
    t_factors = [2500]
    steps = [0.08]
    learn_data_size = 8
    max_traj_len = 21

    num = 1
    iter = list(
        itertools.product(steps, rot_factors, flow_factors, target_factors, t_factors, flow_crits, t_crits, rot_crit))
    for step, rot_factor, flow_factor, target_factor, t_factor, attack_flow_crit, attack_t_crit, attack_rot_crit in iter:
        print(f'iteration num {num} of {len(iter)}')
        run_name = f'attack_flow_crit-{attack_flow_crit}-attack_t_crit-{attack_t_crit}-attack_rot_crit-{attack_rot_crit}-t_factor-{t_factor}-rot_factor-{rot_factor}-flow_factor-{flow_factor}-target_factor-{target_factor}-step-{step}'.replace(
            '_', '-')
        print(run_name)
        args = f'--model-name tartanvo_1914.pkl --kitti --custom_data --test-dir ' \
               f'VO_adv_project_train_dataset_8_frames  --max_traj_len {max_traj_len} --batch-size 1 --worker-num 1 --save_csv ' \
               f'--attack pgd --attack_k {epochs} --alpha {step} --attack_flow_crit {attack_flow_crit} --attack_rot_crit {attack_rot_crit} ' \
               f'--attack_t_crit {attack_t_crit} --attack_target_t_crit patch --attack_norm Linf ' \
               f'--attack_t_factor {t_factor} --attack_rot_factor {rot_factor} --attack_flow_factor {flow_factor} --attack_target_t_factor {target_factor} --run_name {run_name} ' \
               f'--max_traj_datasets {learn_data_size} --save_best_pert'
        os.system(f"python ../run_attacks.py {args}")
        num += 1
# if __name__ == '__main__':
#     epochs = 100
#     flow_crits = ['epe']
#     t_crits = ['partial_rms']
#     rot_crit = ['quat_product_1']
#     t_factors = [1]
#     rot_factors = [1]
#     flow_factors = [1]
#     target_factors = [1]
#     num = 1
#     steps = [0.02, 0.05, 0.07]
#     step = steps[0]
#     learn_data_size = 3
#     iter = list(
#         itertools.product(flow_crits, t_crits, rot_crit, t_factors, rot_factors, flow_factors, target_factors))
#     for attack_flow_crit, attack_t_crit, attack_rot_crit, t_factor, rot_factor, flow_factor, target_factor in list(
#             iter):
#         print(f'iteration num {num} of {len(iter)}')
#         run_name = f'attack_flow_crit-{attack_flow_crit}-attack_t_crit-{attack_t_crit}-attack_rot_crit-{attack_rot_crit}-t_factor-{t_factor}-rot_factor-{rot_factor}-flow_factor-{flow_factor}-target_factor-{target_factor}-step-{step}'.replace(
#             '_', '-')
#         args = f'--model-name tartanvo_1914.pkl --kitti --custom_data --test-dir ' \
#                f'VO_adv_project_train_dataset_8_frames  --max_traj_len {8} --batch-size 1 --worker-num {1} --save_csv ' \
#                f'--attack pgd --attack_k {epochs} --alpha {step} --attack_flow_crit {attack_flow_crit} --attack_rot_crit {attack_rot_crit} ' \
#                f'--attack_t_crit {attack_t_crit} --attack_target_t_crit patch --attack_norm Linf ' \
#                f'--attack_t_factor {t_factor} --attack_rot_factor {rot_factor} --attack_flow_factor {flow_factor} --attack_target_t_factor {target_factor} --run_name {run_name} ' \
#                f'--max_traj_datasets {learn_data_size}'
#         os.system(f"python ../run_attacks.py {args}")
#         num += 1
