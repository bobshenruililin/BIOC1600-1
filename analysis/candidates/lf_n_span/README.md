# Langmuir–Freundlich n-span (Mission 2 candidate)

**Not accepted. Not a flagship. Not occupancy-at-basal restored.** Isolated MODELED analysis of PR #31's claim that unpublished Langmuir–Freundlich *n* can change the withdrawn 81-versus-44000 working-range conclusion.

**Question.** If Hu's surface isotherm is Langmuir–Freundlich with unknown *n*, does the 1:1 81-fold identity still license a device-requirement comparison against a 44000-fold literature-example ratio?

## Rebuild

Python 3 standard library only. No network. No pip.

```bash
sh analysis/candidates/lf_n_span/rebuild.sh
```

## Result (MODELED)

- θ = c^n / (Kd^n + c^n); Kd is c50 for any n > 0.
- 10–90% span = 81^(1/n), independent of Kd.
- n = 1 → 81-fold. n = 0.5 → 6561-fold. n = 2 → 9-fold.
- Matching the labeled 44000-fold Herman/Clements *ratio* as a 10–90% window requires n* ≈ 0.411. Hu's n is UNKNOWN.
- If 1.8 nM is treated as c50, overlay θ(25 nM) is also n-sensitive (≈0.93 at n=1; lower at n<1). That overlay remains a different device (AuED-MEA PBS) and is not PaC tissue occupancy.

## Inference change if correct

The withdrawn flagship cannot be restored without a measured *n* on the relevant construct. The 81-fold identity remains valid supporting biochemistry at n = 1 only.

## Not in this analysis

- Fitting n from Hu figures
- Treating 25 nM / 1.1 mM as retina or as a sensor spec
- Filling glutamate kon/koff
- Docking
