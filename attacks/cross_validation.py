import os
import itertools

if __name__ == '__main__':
    max_traj_len = 8
    worker_num = 1
    attack = 'pgd'
    epochs = 1
    attack_flow_crit = None
    attack_rot_crit = None
    attack_t_crit = 'mean_partial_rms'
    attack_target_t_crit = 'patch'
    t_factor = 1.0
    rot_factor = 1.0
    flow_factor = 1.0
    target_factor = 1.0
    eval_mean = None
    norm = 'Linf'
    window_size = None
    window_stride = None
    steps = [0.001, 0.01, 0.1]
    flow_crits = [None]
    t_crits = ['partial_rms', 'mean_partial_rms', None]
    t_factors = [1, 2]
    rot_factors = [1, 2]
    flow_factors = [1, 2]
    target_factors = [1, 2]
    num = 0
    iter = list(
        itertools.product(flow_crits, t_crits, t_factors, rot_factors, flow_factors, target_factors))
    for attack_flow_crit, attack_t_crit, t_factor, rot_factor, flow_factor, target_factor in iter:
        for step in [0.001, 0.01, 0.1]:
            print(f'iteration num {num} of {len(iter) * 3}')
            run_name = f'attack_flow_crit-{attack_flow_crit}-attack_t_crit-{attack_t_crit}-t_factor-{t_factor}-rot_factor-{rot_factor}-flow_factor-{flow_factor}-target_factor-{target_factor}-step-{step}'.replace(
                '_', '-')
            args = f'--seed {42} --model-name tartanvo_1914.pkl --kitti --custom_data --test-dir ' \
                   f'VO_adv_project_train_dataset_8_frames  --max_traj_len {max_traj_len} --batch-size 1 --worker-num {worker_num} --save_csv ' \
                   f'--attack {attack} --attack_k {epochs} --alpha {step} --attack_flow_crit {attack_flow_crit} --attack_rot_crit {attack_rot_crit} ' \
                   f'--attack_t_crit {attack_t_crit} --attack_target_t_crit {attack_target_t_crit} --attack_norm {norm} ' \
                   f'--attack_t_factor {t_factor} --attack_rot_factor {rot_factor} --attack_flow_factor {flow_factor} --attack_target_t_factor {target_factor} --run_name {run_name}'
            os.system(f"python ../run_attacks.py {args}")
            num += 1
