# a = #ctl00_SPWebPartManager1_g_5f765d3f_f705_4af4_83e7_cd16b175ab26_ctl00_rptSearchJobs_ctl02_lblStateName
# b = 

demo = "ctl00_SPWebPartManager1_g_5f765d3f_f705_4af4_83e7_cd16b175ab26_ctl00_rptSearchJobs_ctl02_lblJobTitle"
new = demo.rsplit('ct',1)[0]
for a in range(101, 111):
    link = f'{new}ct{a}_lblJobTitle'
    print(link)