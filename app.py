{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "cd63be89",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "ERROR: Could not find a version that satisfies the requirement pickle (from versions: none)\n",
      "ERROR: No matching distribution found for pickle\n"
     ]
    }
   ],
   "source": [
    "#!pip install streamlit\n",
    "!pip install pickle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0758f523",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "e88bbe39",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026-07-26 21:49:30.221 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-07-26 21:49:31.170 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run c:\\ProgramData\\anaconda3\\envs\\scottenv\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2026-07-26 21:49:31.172 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-07-26 21:49:31.173 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-07-26 21:49:31.175 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-07-26 21:49:31.176 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-07-26 21:49:31.177 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-07-26 21:49:31.178 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-07-26 21:49:31.179 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-07-26 21:49:31.180 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-07-26 21:49:31.181 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-07-26 21:49:31.182 Session state does not function when running a script without `streamlit run`\n",
      "2026-07-26 21:49:31.183 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-07-26 21:49:31.184 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-07-26 21:49:31.185 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-07-26 21:49:31.186 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-07-26 21:49:31.187 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-07-26 21:49:31.187 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-07-26 21:49:31.189 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-07-26 21:49:31.190 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-07-26 21:49:31.190 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-07-26 21:49:31.191 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-07-26 21:49:31.192 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-07-26 21:49:31.192 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-07-26 21:49:31.193 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-07-26 21:49:31.193 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-07-26 21:49:31.194 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-07-26 21:49:31.195 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-07-26 21:49:31.195 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-07-26 21:49:31.199 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-07-26 21:49:31.199 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-07-26 21:49:31.200 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "ename": "StreamlitMixedNumericTypesError",
     "evalue": "All numerical arguments must be of the same type.\n`value` has str type.\n`step` has int type.",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mStreamlitMixedNumericTypesError\u001b[39m           Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[5]\u001b[39m\u001b[32m, line 48\u001b[39m\n\u001b[32m     44\u001b[39m room_type = st.selectbox(\u001b[33m\"\u001b[39m\u001b[33mSelect room type\u001b[39m\u001b[33m\"\u001b[39m, TYPE)\n\u001b[32m     47\u001b[39m \u001b[38;5;66;03m# photo count\u001b[39;00m\n\u001b[32m---> \u001b[39m\u001b[32m48\u001b[39m photo_count = \u001b[43mst\u001b[49m\u001b[43m.\u001b[49m\u001b[43mnumber_input\u001b[49m\u001b[43m(\u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mNumber of photos you plan to take?\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mmin_value\u001b[49m\u001b[43m=\u001b[49m\u001b[32;43m0.0\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mstep\u001b[49m\u001b[43m=\u001b[49m\u001b[32;43m1\u001b[39;49m\u001b[43m)\u001b[49m\n\u001b[32m     51\u001b[39m \u001b[38;5;66;03m# guest count\u001b[39;00m\n\u001b[32m     52\u001b[39m guest_count = st.number_input(\u001b[33m\"\u001b[39m\u001b[33mNumber of guests you can accomodate\u001b[39m\u001b[33m\"\u001b[39m, min_value=\u001b[32m0.0\u001b[39m, step=\u001b[32m1\u001b[39m)\n",
      "\u001b[36mFile \u001b[39m\u001b[32mc:\\ProgramData\\anaconda3\\envs\\scottenv\\Lib\\site-packages\\streamlit\\runtime\\metrics_util.py:447\u001b[39m, in \u001b[36mgather_metrics.<locals>.wrapped_func\u001b[39m\u001b[34m(*args, **kwargs)\u001b[39m\n\u001b[32m    445\u001b[39m         _LOGGER.debug(\u001b[33m\"\u001b[39m\u001b[33mFailed to collect command telemetry\u001b[39m\u001b[33m\"\u001b[39m, exc_info=ex)\n\u001b[32m    446\u001b[39m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[32m--> \u001b[39m\u001b[32m447\u001b[39m     result = \u001b[43mnon_optional_func\u001b[49m\u001b[43m(\u001b[49m\u001b[43m*\u001b[49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m*\u001b[49m\u001b[43m*\u001b[49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m    448\u001b[39m \u001b[38;5;28;01mexcept\u001b[39;00m RerunException:\n\u001b[32m    449\u001b[39m     \u001b[38;5;66;03m# Duplicated from below, because static analysis tools get confused\u001b[39;00m\n\u001b[32m    450\u001b[39m     \u001b[38;5;66;03m# by deferring the rethrow.\u001b[39;00m\n\u001b[32m    451\u001b[39m     \u001b[38;5;28;01mif\u001b[39;00m tracking_activated \u001b[38;5;129;01mand\u001b[39;00m command_telemetry:\n",
      "\u001b[36mFile \u001b[39m\u001b[32mc:\\ProgramData\\anaconda3\\envs\\scottenv\\Lib\\site-packages\\streamlit\\elements\\widgets\\number_input.py:399\u001b[39m, in \u001b[36mNumberInputMixin.number_input\u001b[39m\u001b[34m(self, label, min_value, max_value, value, step, format, key, help, on_change, args, kwargs, placeholder, disabled, label_visibility, icon, width)\u001b[39m\n\u001b[32m    235\u001b[39m \u001b[38;5;250m\u001b[39m\u001b[33mr\u001b[39m\u001b[33;03m\"\"\"Display a numeric input widget.\u001b[39;00m\n\u001b[32m    236\u001b[39m \n\u001b[32m    237\u001b[39m \u001b[33;03m.. note::\u001b[39;00m\n\u001b[32m   (...)\u001b[39m\u001b[32m    396\u001b[39m \n\u001b[32m    397\u001b[39m \u001b[33;03m\"\"\"\u001b[39;00m\n\u001b[32m    398\u001b[39m ctx = get_script_run_ctx()\n\u001b[32m--> \u001b[39m\u001b[32m399\u001b[39m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43m_number_input\u001b[49m\u001b[43m(\u001b[49m\n\u001b[32m    400\u001b[39m \u001b[43m    \u001b[49m\u001b[43mlabel\u001b[49m\u001b[43m=\u001b[49m\u001b[43mlabel\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    401\u001b[39m \u001b[43m    \u001b[49m\u001b[43mmin_value\u001b[49m\u001b[43m=\u001b[49m\u001b[43mmin_value\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    402\u001b[39m \u001b[43m    \u001b[49m\u001b[43mmax_value\u001b[49m\u001b[43m=\u001b[49m\u001b[43mmax_value\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    403\u001b[39m \u001b[43m    \u001b[49m\u001b[43mvalue\u001b[49m\u001b[43m=\u001b[49m\u001b[43mvalue\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    404\u001b[39m \u001b[43m    \u001b[49m\u001b[43mstep\u001b[49m\u001b[43m=\u001b[49m\u001b[43mstep\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    405\u001b[39m \u001b[43m    \u001b[49m\u001b[38;5;28;43mformat\u001b[39;49m\u001b[43m=\u001b[49m\u001b[38;5;28;43mformat\u001b[39;49m\u001b[43m,\u001b[49m\n\u001b[32m    406\u001b[39m \u001b[43m    \u001b[49m\u001b[43mkey\u001b[49m\u001b[43m=\u001b[49m\u001b[43mkey\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    407\u001b[39m \u001b[43m    \u001b[49m\u001b[43mhelp\u001b[49m\u001b[43m=\u001b[49m\u001b[43mhelp\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    408\u001b[39m \u001b[43m    \u001b[49m\u001b[43mon_change\u001b[49m\u001b[43m=\u001b[49m\u001b[43mon_change\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    409\u001b[39m \u001b[43m    \u001b[49m\u001b[43margs\u001b[49m\u001b[43m=\u001b[49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    410\u001b[39m \u001b[43m    \u001b[49m\u001b[43mkwargs\u001b[49m\u001b[43m=\u001b[49m\u001b[43mkwargs\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    411\u001b[39m \u001b[43m    \u001b[49m\u001b[43mplaceholder\u001b[49m\u001b[43m=\u001b[49m\u001b[43mplaceholder\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    412\u001b[39m \u001b[43m    \u001b[49m\u001b[43mdisabled\u001b[49m\u001b[43m=\u001b[49m\u001b[43mdisabled\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    413\u001b[39m \u001b[43m    \u001b[49m\u001b[43mlabel_visibility\u001b[49m\u001b[43m=\u001b[49m\u001b[43mlabel_visibility\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    414\u001b[39m \u001b[43m    \u001b[49m\u001b[43micon\u001b[49m\u001b[43m=\u001b[49m\u001b[43micon\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    415\u001b[39m \u001b[43m    \u001b[49m\u001b[43mwidth\u001b[49m\u001b[43m=\u001b[49m\u001b[43mwidth\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    416\u001b[39m \u001b[43m    \u001b[49m\u001b[43mctx\u001b[49m\u001b[43m=\u001b[49m\u001b[43mctx\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    417\u001b[39m \u001b[43m\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[36mFile \u001b[39m\u001b[32mc:\\ProgramData\\anaconda3\\envs\\scottenv\\Lib\\site-packages\\streamlit\\elements\\widgets\\number_input.py:482\u001b[39m, in \u001b[36mNumberInputMixin._number_input\u001b[39m\u001b[34m(self, label, min_value, max_value, value, step, format, key, help, on_change, args, kwargs, placeholder, disabled, label_visibility, icon, width, ctx)\u001b[39m\n\u001b[32m    477\u001b[39m all_float_args = \u001b[38;5;28mall\u001b[39m(\n\u001b[32m    478\u001b[39m     \u001b[38;5;28misinstance\u001b[39m(a, (\u001b[38;5;28mfloat\u001b[39m, \u001b[38;5;28mtype\u001b[39m(\u001b[38;5;28;01mNone\u001b[39;00m), \u001b[38;5;28mstr\u001b[39m)) \u001b[38;5;28;01mfor\u001b[39;00m a \u001b[38;5;129;01min\u001b[39;00m number_input_args\n\u001b[32m    479\u001b[39m )\n\u001b[32m    481\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m all_int_args \u001b[38;5;129;01mand\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m all_float_args:\n\u001b[32m--> \u001b[39m\u001b[32m482\u001b[39m     \u001b[38;5;28;01mraise\u001b[39;00m StreamlitMixedNumericTypesError(\n\u001b[32m    483\u001b[39m         value=value, min_value=min_value, max_value=max_value, step=step\n\u001b[32m    484\u001b[39m     )\n\u001b[32m    486\u001b[39m session_state = get_session_state().filtered_state\n\u001b[32m    487\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m key \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m \u001b[38;5;129;01mand\u001b[39;00m key \u001b[38;5;129;01min\u001b[39;00m session_state \u001b[38;5;129;01mand\u001b[39;00m session_state[key] \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n",
      "\u001b[31mStreamlitMixedNumericTypesError\u001b[39m: All numerical arguments must be of the same type.\n`value` has str type.\n`step` has int type."
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pickle\n",
    "import numpy as np\n",
    "import sklearn\n",
    "import pandas as pd\n",
    "\n",
    "def load_model():\n",
    "    try:\n",
    "        with open(\"mountainapp.pkl\", \"rb\") as f:\n",
    "            model = pickle.load(f)\n",
    "        return model\n",
    "    except FileNotFoundError:\n",
    "        st.error(\"Model file not found. Please ensure 'iris_model.pkl' is in the same directory.\")\n",
    "        return None\n",
    "    except Exception as e:\n",
    "        st.error(f\"Error loading model: {e}\")\n",
    "        return None\n",
    "\n",
    "model = load_model()\n",
    "\n",
    "st.title(\"Mountain airBNB profit predicting app\")\n",
    "st.write(\"Enter the listing shizz\")\n",
    "\n",
    "# Input fields\n",
    "\n",
    "\n",
    "\n",
    "# ['revenue', 'STARTmonth','region_x','room_type','photos_count','guests','bedrooms','beds','baths','professional_management','min_nights', 'City']\n",
    "# pd.get_dummies(front_mountains, columns=['STARTmonth','region_x','room_type','City'], drop_first=True)\n",
    "\n",
    "# Month selector\n",
    "# Month names\n",
    "MONTHS = ('January', 'February', 'March', 'April', 'May', 'June',\n",
    "'July', 'August', 'September', 'October', 'November', 'December')\n",
    "selected_month = st.selectbox(\"Select month to start\", MONTHS)\n",
    "\n",
    "# region selector\n",
    "REGION = ('Mountain','Piedmont/Central','Beach')\n",
    "selected_region = st.selectbox(\"Select region to host in\", REGION)\n",
    "\n",
    "\n",
    "# room type\n",
    "TYPE = ('entire_home', 'hotel_room', 'unique_location', 'private_room')\n",
    "room_type = st.selectbox(\"Select room type\", TYPE)\n",
    "\n",
    "\n",
    "# photo count\n",
    "photo_count = st.number_input(\"Number of photos you plan to take?\", min_value=0.0, step=1)\n",
    "\n",
    "\n",
    "# guest count\n",
    "guest_count = st.number_input(\"Number of guests you can accomodate\", min_value=0.0, step=1)\n",
    "\n",
    "\n",
    "#bedrooms\n",
    "bedroom = st.number_input(\"Number of bedrooms\", min_value=0.0, step=1)\n",
    "\n",
    "# baths\n",
    "baths = st.number_input(\"Number of bathrooms\", min_value=0.0, step=0.5)\n",
    "\n",
    "\n",
    "#managed?\n",
    "MANAGE = ('True','False')\n",
    "managed = st.selectbox(\"Will it be professionally managed?\", MANAGE)\n",
    "\n",
    "\n",
    "#nights\n",
    "nights = st.number_input(\"Min nights to stay\", min_value=0.0, step=1)\n",
    "\n",
    "# city\n",
    "CITIES = ('Asheville', 'Carolina Beach', 'Charlotte', 'Durham', 'Gatlinburg',\n",
    "       'Myrtle Beach', 'Pigeon Forge', 'Raleigh', 'Williamsburg',\n",
    "       'Wilmington')\n",
    "city = st.selectbox(\"What city\", CITIES)\n",
    "\n",
    "\n",
    "input_data = pd.DataFrame({\n",
    "    \"Month\": [selected_month],\n",
    "    \"Region\": [selected_region],\n",
    "    \"Room type\": [room_type],\n",
    "    \"Photo count\": [photo_count],\n",
    "    \"Guest count\": [guest_count],\n",
    "    \"# bedrooms\": [bedroom],\n",
    "    \"baths\": [baths],\n",
    "    \"Professionally managed?\": [managed],\n",
    "    \"min nights\": [nights],\n",
    "    \"city\": [city]\n",
    "})\n",
    "\n",
    "input_data_encoded = pd.get_dummies(input_data, columns=['Month','Region','Room type','Professionally managed?','city'])\n",
    "\n",
    "model_columns = model.feature_names_in_\n",
    "for col in model_columns:\n",
    "    if col not in input_data_encoded.columns:\n",
    "        input_data_encoded[col] = 0\n",
    "\n",
    "input_data_encoded = input_data_encoded[model_columns]\n",
    "\n",
    "\n",
    "if st.button(\"Predict\"):\n",
    "    prediction = model.predict(input_data_encoded)[0]\n",
    "    st.write(prediction)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e948e55a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "^C\n",
      "fetching tunnel pass\n"
     ]
    },
    {
     "ename": "OSError",
     "evalue": "Background processes not supported.",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mOSError\u001b[39m                                   Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[8]\u001b[39m\u001b[32m, line 4\u001b[39m\n\u001b[32m      1\u001b[39m get_ipython().system(\u001b[33m'\u001b[39m\u001b[33mstreamlit run c:/ProgramData/anaconda3/envs/scottenv/Lib/site-packages/ipykernel_launcher.py\u001b[39m\u001b[33m'\u001b[39m)\n\u001b[32m      3\u001b[39m \u001b[38;5;28mprint\u001b[39m(\u001b[33m\"\u001b[39m\u001b[33mfetching tunnel pass\u001b[39m\u001b[33m\"\u001b[39m)\n\u001b[32m----> \u001b[39m\u001b[32m4\u001b[39m \u001b[43mget_ipython\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\u001b[43m.\u001b[49m\u001b[43msystem\u001b[49m\u001b[43m(\u001b[49m\u001b[33;43m'\u001b[39;49m\u001b[33;43mcurl https://loca.lt/mytunnelpassword &\u001b[39;49m\u001b[33;43m'\u001b[39;49m\u001b[43m)\u001b[49m\n\u001b[32m      6\u001b[39m \u001b[38;5;66;03m# start tunnel\u001b[39;00m\n\u001b[32m      7\u001b[39m get_ipython().system(\u001b[33m'\u001b[39m\u001b[33mnpx localtunnel --port 8501\u001b[39m\u001b[33m'\u001b[39m)\n",
      "\u001b[36mFile \u001b[39m\u001b[32mc:\\ProgramData\\anaconda3\\envs\\scottenv\\Lib\\site-packages\\ipykernel\\zmqshell.py:694\u001b[39m, in \u001b[36mZMQInteractiveShell.system_piped\u001b[39m\u001b[34m(self, cmd)\u001b[39m\n\u001b[32m    687\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m cmd.rstrip().endswith(\u001b[33m\"\u001b[39m\u001b[33m&\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m    688\u001b[39m     \u001b[38;5;66;03m# this is *far* from a rigorous test\u001b[39;00m\n\u001b[32m    689\u001b[39m     \u001b[38;5;66;03m# We do not support backgrounding processes because we either use\u001b[39;00m\n\u001b[32m    690\u001b[39m     \u001b[38;5;66;03m# pexpect or pipes to read from.  Users can always just call\u001b[39;00m\n\u001b[32m    691\u001b[39m     \u001b[38;5;66;03m# os.system() or use ip.system=ip.system_raw\u001b[39;00m\n\u001b[32m    692\u001b[39m     \u001b[38;5;66;03m# if they really want a background process.\u001b[39;00m\n\u001b[32m    693\u001b[39m     msg = \u001b[33m\"\u001b[39m\u001b[33mBackground processes not supported.\u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m--> \u001b[39m\u001b[32m694\u001b[39m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mOSError\u001b[39;00m(msg)\n\u001b[32m    696\u001b[39m \u001b[38;5;66;03m# we explicitly do NOT return the subprocess status code, because\u001b[39;00m\n\u001b[32m    697\u001b[39m \u001b[38;5;66;03m# a non-None value would trigger :func:`sys.displayhook` calls.\u001b[39;00m\n\u001b[32m    698\u001b[39m \u001b[38;5;66;03m# Instead, we store the exit_code in user_ns.\u001b[39;00m\n\u001b[32m    699\u001b[39m \u001b[38;5;66;03m# Also, protect system call from UNC paths on Windows here too\u001b[39;00m\n\u001b[32m    700\u001b[39m \u001b[38;5;66;03m# as is done in InteractiveShell.system_raw\u001b[39;00m\n\u001b[32m    701\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m sys.platform == \u001b[33m\"\u001b[39m\u001b[33mwin32\u001b[39m\u001b[33m\"\u001b[39m:\n",
      "\u001b[31mOSError\u001b[39m: Background processes not supported."
     ]
    }
   ],
   "source": [
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "scottenv",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
